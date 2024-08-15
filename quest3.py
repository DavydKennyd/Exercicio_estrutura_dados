from binarytree import bst, Node

no = bst(height=4)


def pre(no):
    if no is None:
        return
    print(no.value)
    pre(no.left)
    pre(no.right)

print(no)

pre(no)