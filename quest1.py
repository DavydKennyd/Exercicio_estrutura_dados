from binarytree import bst, Node

no = bst(height=4)
no.left = Node(5)
no.left.left = Node(2)
def pre(no):
    if no is None:
        return
    print(no.value)
    pre(no.left)
    pre(no.right)


def em_ordem(no):
    if no is None:
        return
    em_ordem(no.left)
    print(no.value)
    em_ordem(no.right)


def pos_ordem(no):
    if no is None:
        return
    pos_ordem(no.left)
    pos_ordem(no.right)
    print(no.value)

print(no)

print("EM PRÉ-ORDEM")
pre(no)
print("EM ORDEM")
em_ordem(no)
print("EM PÓS-ORDEM")
pos_ordem(no)
