class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            steps = 1
            self._insert(val, self.root, steps)

    def _insert(self, val, node, steps):
        if val < node.val:
            if not node.left:
                node.left = TreeNode(val)
            else:
                self._insert(val, node.left, steps)
        if val > node.val:
            if not node.right:
                node.right = TreeNode(val)
            else:
                self._insert(val, node.right, steps)

    def delete(self, val):
        self._delete(val, self.root)

    def _delete(self, val, node):
        # Node not found.
        if not node:
            return None
        # Finding given node.
        elif val < node.val:
            node.left = self._delete(val, node.left)
        elif val > node.val:
            node.right = self._delete(val, node.right)
        else:
            # Deleting found node.
            # If there's no leaves, just remove node.
            if not node.left and not node.right:
                node = None
            # If there are leaves, connect them to the tree.
            elif not node.left:
                node = node.right
            elif not node.right:
                node = node.left
            # If there are both leaves and nodes above, elevate the node
            else:
                min_node = self._find_min(node.right)
                node.val = min_node.val
                node.right = self._delete(min_node.val, node.right)
        return node

    # Helper function for delete.
    def _find_min(self, node):
        while node.left:
            node = node.left
        return node
    
    def search(self, val):
        steps = 0
        return self._search(val, self.root, steps)

    def _search(self, val, node, steps):
        if not node:
            return False, steps
        elif node.val == val:
            steps += 1
            return True, steps
        elif node.val > val:
            steps += 1
            return self._search(val, node.left, steps)
        else:
            steps += 1
            return self._search(val, node.right, steps)

    def print_tree(self):
        lines, *_ = self._print_tree(self.root)
        print("=============== Binary Search Tree ===============")
        for line in lines:
            print(line)
        print("==================================================")

    def _print_tree(self, node):
        # No wings.
        if node.right is None and node.left is None:
            line = '%s' % node.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # No right wing.
        if node.right is None:
            lines, n, p, x = self._print_tree(node.left)
            s = '%s' % node.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # No left wing.
        if node.left is None:
            lines, n, p, x = self._print_tree(node.right)
            s = '%s' % node.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Both wings.
        left, n, p, x = self._print_tree(node.left)
        right, m, q, y = self._print_tree(node.right)
        s = '%s' % node.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2