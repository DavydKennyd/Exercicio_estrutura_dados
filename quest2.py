from binarytree import bst, Node

arvore = bst(height=4)

def inserir(no, novo):
    if no is None:
        return Node(novo)
    
    if novo < no.value:
        no.left = inserir(no.left, novo)
    else:
        no.right = inserir(no.right, novo)
    
    return no

novo_numeros = [5, 2]

print("Árvore antes de inserir os números:")
print(arvore)

for numero in novo_numeros:
    arvore = inserir(arvore, numero)

print("Árvore depois de inserir os números:")
print(arvore)


print("CONSEGUI PORRA!!!!")