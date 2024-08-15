from binarytree import bst, Node


no = bst(height=4)


def encontra_numero(no, valor):
    if no is None:
        return False
    if no.value == valor:
        return True
    elif valor < no.value:
        return encontra_numero(no.left, valor)
    else:
        return encontra_numero(no.right, valor)


print(no)

encontra = 6
if encontra_numero(no,encontra):
    print(f"O numero {encontra} foi encotrado na arvore")

else:
    print(f"O numero {encontra} não foi encontrado")
