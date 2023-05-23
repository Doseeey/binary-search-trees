from bst import BST
from redblack import RedBlackTree
from avl import AVLTree
from random import randint
from datetime import datetime
import csv

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

def search_and_delete(tree, values):
    results = {}
    for value in values:
        s = tree.search(value)
        if s[1]:
            print(f"Found {value} after {s[1]} steps. Now deleting value from the tree.")
            tree.delete(value)
            results[value] = s[1]
    return results

def insert_time_benchmark(tree):
    #Benchmark for 10000 inserts
    size = 20000
    values = values_list(size)

    for i in range(size-1):
        start = datetime.now()
        tree.insert(values[i])
        stop = datetime.now()
        print(f"{i+1}: {stop-start}")

if __name__ == "__main__":
    t1 = BST()
    t2 = RedBlackTree()
    t3 = AVLTree()

    values = values_list(10)
    #print(values)
    #values = [6, 10, 7, 8, 2, 9, 5, 3, 1, 4]
    for i in values:
        t1.insert(i)
        t2.insert(i)
        t3.insert(i)

    t1.print_tree()
    t2.print_tree()
    t3.print_tree()
    # values = [10, 25, 55, 900, 473, 478, 484, 233, 555, 111]
    # r1 = search_and_delete(t1, values)
    # r2 = search_and_delete(t2, values)
    # r3 = search_and_delete(t3, values)

    # print("====Summary Table====")
    # print("Value ----- BST ------ RedBlack ----- AVL")
    # for value in values:
    #     print(f"{value} ----- {r1[value]} ----- {r2[value]} ----- {r3[value]}")

    # t1.print_tree()
    # t2.print_tree()
    # t3.print_tree()