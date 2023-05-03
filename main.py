from bst import BST
from random import randint

def values_list(size):
    values = []
    while len(values) != size:
        val = randint(0, size)
        if val not in values:
            values.append(val)
    return values

def fill_tree(tree, size):
    values = values_list(size)
    for i in range(size-1):
        tree.insert(values[i])

if __name__ == "__main__":
    t1 = BST()
    fill_tree(t1, 50)

    t1.print_tree()

    lookup_number = 9
    found = t1.search(lookup_number)
    if found[0]:
        print(f"Node with value {lookup_number} found after {found[1]} steps.")
    else:
        print(f"Node with value {lookup_number} not found.")
    
