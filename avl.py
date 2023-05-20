class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)
    
    def _insert(self, node, value):
        if node is None:
            return Node(value)
        elif value < node.val:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        #Calculate height
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)

        #All cases
        if balance > 1 and value < node.left.val:
            return self._right_rotate(node)
        if balance < -1 and value > node.right.val:
            return self._left_rotate(node)
        if balance > 1 and value > node.left.val:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and value < node.right.val:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node 

    def delete(self, value):
        self.root = self._delete(self.root, value)
    
    def _delete(self, node, value):
        if node is None:
            return node
        
        if value < node.val:
            node.left = self._delete(node.left, value)
        elif value > node.val:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            
            temp = self._get_minimum(node.right)
            node.val = temp.val
            node.right = self._delete(node.right, temp.val)

        #Calculate height
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)

        #All cases
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        
        return node
    
    def search(self, value):
        steps = 0
        return self._search_node(self.root, value, steps)

    def _search_node(self, root, value, steps):
        if not root or root.val == value:
            steps += 1
            return True, steps

        if value < root.val:
            steps += 1
            return self._search_node(root.left, value, steps)
        else:
            steps += 1
            return self._search_node(root.right, value, steps)
        

    def _left_rotate(self, node):
        edonR = node.right
        tempLeft = edonR.left

        edonR.left = node
        node.right = tempLeft

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        edonR.height = 1 + max(self._get_height(edonR.left), self._get_height(edonR.right))

        return edonR
    
    def _right_rotate(self, node):
        edonL = node.left
        tempRight = edonL.right

        edonL.right = node
        node.left = tempRight

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        edonL.height = 1 + max(self._get_height(edonL.left), self._get_height(edonL.right))

        return edonL
    
    def _get_height(self, node):
        if node is None:
            return 0
        return node.height
    
    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    def _get_minimum(self, node):
        while node.left != None:
            node = node.left
        return node
    
    def print_tree(self):
        lines, *_ = self._print_tree(self.root)
        print("==================== AVL Tree ====================")
        for line in lines:
            print(line)
        print("==================================================")

    def _print_tree(self, node):
        # No wings.
        if node.right is None and node.left is None:
            line = f'{node.val} ({node.height})'
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # No right wing.
        if node.right is None:
            lines, n, p, x = self._print_tree(node.left)
            s = f'{node.val} ({node.height})'
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # No left wing.
        if node.left is None:
            lines, n, p, x = self._print_tree(node.right)
            s = f'{node.val} ({node.height})'
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Both wings.
        left, n, p, x = self._print_tree(node.left)
        right, m, q, y = self._print_tree(node.right)
        s = f'{node.val} ({node.height})'
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
        