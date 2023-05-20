from bst import BST
from redblack import RedBlackTree
from avl import AVLTree
from random import randint
from datetime import datetime

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

def fill_time_comparision(type):
    print(f"\nInsertion times for {type}:")
    for size in [1000, 5000, 10000, 20000, 30000, 50000]:
        start = datetime.now()
        if type == "BST":
            tree = BST()
        elif type == "RedBlack":
            tree = RedBlackTree()
        elif type == "AVL":
            tree = AVLTree()
        else: 
            print("Wrong type, choose correct type: BST, RedBlack, AVL")
            return
        
        fill_tree(tree, size)
        stop = datetime.now()

        print(f" - Inserting {size} elements took {stop - start} time.")
    return

if __name__ == "__main__":
    t1 = BST()
    fill_tree(t1, 50)
    fill_time_comparision("BST")
    fill_time_comparision("RedBlack")
    fill_time_comparision("AVL")
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

    # t3 = AVLTree()
    # fill_tree(t3, 10)
    # t3.print_tree()
    # z = t3.search(8)
    # print(z[1])