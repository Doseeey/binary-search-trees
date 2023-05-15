from bst import BST
from redblack import RedBlackTree
from avl import AVLTree
from random import randint

def values_list(size):
    values = []
    while len(values) != size:
        val = randint(1, size)
        if val not in values:
            values.append(val)
    return values

def fill_tree(tree, size):
    values = values_list(size)
    for i in range(size-1):
        tree.insert(values[i])

if __name__ == "__main__":
    # t1 = BST()
    # fill_tree(t1, 50)

    # t1.print_tree()

    # lookup_number = 9
    # found = t1.search(lookup_number)
    # if found[0]:
    #     print(f"Node with value {lookup_number} found after {found[1]} steps.")
    # else:
    #     print(f"Node with value {lookup_number} not found.")
    
    # t2 = RedBlackTree()
    # fill_tree(t2, 10)

    # t2.print_tree()

    # t2.delete_node(1)

    # t2.print_tree()

    # lookup_number = 9
    # found = t2.search(lookup_number)
    # if found[0]:
    #     print(f"Node with value {lookup_number} found after {found[1]} steps.")
    # else:
    #     print(f"Node with value {lookup_number} not found.")

    t3 = AVLTree()
    fill_tree(t3, 10)
    t3.print_tree()
