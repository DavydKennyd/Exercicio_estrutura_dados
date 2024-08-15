from binarytree import bst, Node

no = bst(height=4)

def pos_ordem(no):
    if no is None:
        return
    pos_ordem(no.left)
    pos_ordem(no.right)
    print(no.value)


print(no)

pos_ordem(no)