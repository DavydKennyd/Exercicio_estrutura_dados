from binarytree import bst, Node

no = bst(height=4)

def em_ordem(no):
    if no is None:
        return
    
    em_ordem(no.left)
    print(no.value)
    em_ordem(no.right)


print(no)

em_ordem(no)