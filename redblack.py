class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        #1/0 Red/Black
        self.color = 1

class RedBlackTree:
    def __init__(self):
        self.nil = Node(0)
        self.nil.color = 0
        self.root = self.nil

    def insert(self, val):
        node = Node(val)
        node.left = self.nil
        node.right = self.nil
        node.parent = None

        if self.root == self.nil:
            self.root = node
            node.color = 0
        else:
            curr = self.root
            while curr != self.nil:
                node.parent = curr
                if node.val < curr.val:
                    curr = curr.left
                else:
                    curr = curr.right

            node.color = 1
            node.parent = node.parent

            if node.parent == None:
                self.root = node
            elif node.val < node.parent.val:
                node.parent.left = node
            else:
                node.parent.right = node

            self._insert_fix(node)

    def insert_bulk(self, arr):
        for val in arr:
            node = Node(val)
            node.left = self.nil
            node.right = self.nil
            node.parent = None

            if self.root == self.nil:
                self.root = node
                node.color = 0
            else:
                curr = self.root
                while curr != self.nil:
                    node.parent = curr
                    if node.val < curr.val:
                        curr = curr.left
                    else:
                        curr = curr.right

                node.color = 1
                node.parent = node.parent

                if node.parent == None:
                    self.root = node
                elif node.val < node.parent.val:
                    node.parent.left = node
                else:
                    node.parent.right = node

        self._insert_fix(node)

    def _insert_fix(self, node):
        while node.parent.color: #while red
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.left
                if uncle.color:
                    uncle.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.left_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.right

                if uncle.color == 1:
                    uncle.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.right_rotate(node.parent.parent)
                    
            if node == self.root:
                break

        self.root.color = 0

    def left_rotate(self, node):
        edon = node.right
        node.right = edon.left
        
        if edon.left != self.nil:
            edon.left.parent = node
        
        edon.parent = node.parent
        if node.parent == None:
            self.root = edon
        elif node == node.parent.left:
            node.parent.left = edon
        else:
            node.parent.right = edon
        
        edon.left = node
        node.parent = edon

    def right_rotate(self, node):
        edon = node.left
        node.left = edon.right

        if edon.right != self.nil:
            self.root = edon
        
        edon.parent = node.parent
        if node.parent == None:
            self.root = edon
        elif node == node.parent.right:
            node.parent.right = edon
        else:
            node.parent.left = edon
        
        edon.right = node
        node.parent = edon

    def search(self, val):
        steps = 0
        return self._search(val, steps)
    
    def _search(self, val, steps):
        curr = self.root
        steps += 1
        while curr != self.nil and val != curr.val:
            if val < curr.val:
                curr = curr.left
                steps += 1
            else:
                curr = curr.right
                steps += 1
        
        if curr == self.nil:
            return False, steps
        else:
            return True, steps
    
    def delete(self, val):
        return self._delete(self.root, val) 

    def _delete(self, node, val):
        z = self.nil
        while node != self.nil:
            if node.val == val:
                z = node
            if node.val <= val:
                node = node.right
            else:
                node = node.left

        if z == self.nil:
            return
        
        temp = z
        temp_original_color = temp.color

        if z.left == self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.transplant(z, z.left)
        else:
            temp = self.minimum(z.right)
            temp_original_color = temp.color
            x = temp.right

            if temp.parent == z:
                x.parent = temp
            else:
                self.transplant(temp, temp.right)
                temp.right = z.right
                temp.right.parent = temp

            self.transplant(z, temp)
            temp.left = z.left
            temp.left.parent = temp
            temp.color = z.color

        if temp_original_color == 0:
            self._delete_fix(x)

    def _delete_fix(self, node):
        while node != self.root and node.color == 0:
            if node == node.parent.left:
                s = node.parent.right
                if s.color:
                    s.color = 0
                    node.parent.color = 1
                    self.left_rotate(node.parent)
                    s = node.parent.right
                
                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    node = node.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = node.parent.right

                    s.color = node.parent.color
                    node.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(node.parent)
                    node = self.root
            else:
                s = node.parent.left
                if s.color:
                    s.color = 0
                    node.parent.color = 1
                    self.right_rotate(node.parent)
                    s = node.parent.left
                
                if s.right.color == 0 and s.left.color == 0:
                    s.color = 1
                    node = node.parent
                else:
                    if s.left.color == 0:
                        s.right.color == 0
                        s.color = 1
                        self.left_rotate(s)
                        s = node.parent.left
                
                s.color = node.parent.color
                node.parent.color = 0
                s.left.color = 0
                self.right_rotate(node.parent)
                node = self.root
        node.color = 0

    def minimum(self, node):
        while node.left != self.nil:
            node = node.left
        return node

    def transplant(self, a, b):
        if a.parent == None:
            self.root = b
        elif a == a.parent.left:
            a.parent.left = b
        else:
            a.parent.right = a
        a.parent = b.parent

    def print_tree(self):
        lines, *_ = self._print_tree(self.root)
        print("================= Red Black Tree =================")
        for line in lines:
            print(line)
        print("==================================================")

    def _print_tree(self, node):
        # No wings.
        if node.right is None and node.left is None:
            color = "R" if node.color == 1 else "B"
            if node.val:    
                line = f'{color}: {node.val}'
            else:
                line = f'NIL'
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # No right wing.
        if node.right is None:
            lines, n, p, x = self._print_tree(node.left)
            color = "R" if node.color == 1 else "B"
            if node.val:    
                s = f'{color}: {node.val}'
            else:
                s = f'NIL'
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # No left wing.
        if node.left is None:
            lines, n, p, x = self._print_tree(node.right)
            color = "R" if node.color == 1 else "B"
            if node.val:    
                s = f'{color}: {node.val}'
            else:
                s = f'NIL'
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Both wings.
        left, n, p, x = self._print_tree(node.left)
        right, m, q, y = self._print_tree(node.right)
        color = "R" if node.color == 1 else "B"
        if node.val:    
                s = f'{color}: {node.val}'
        else:
            s = f'NIL'
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
    