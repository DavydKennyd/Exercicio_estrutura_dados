from binarytree import bst, Node

no = bst(height=4)

def remove_numero(arvore, valor):
    if arvore is None:
        return arvore
    
    if valor < arvore.value:
        arvore.left = remove_numero(arvore.left, valor)
    elif valor > arvore.value:
        arvore.right = remove_numero(arvore.right, valor)
    else:
        if arvore.left is None:
            return arvore.right
        elif arvore.right is None:
            return arvore.left
        
        min_larger_node = arvore.right
        while min_larger_node.left is not None:
            min_larger_node = min_larger_node.left
        
        arvore.value = min_larger_node.value
        arvore.right = remove_numero(arvore.right, min_larger_node.value)
    
    return arvore

def numero_existe(arvore, valor):
    if arvore is None:
        return False
    if arvore.value == valor:
        return True
    elif valor < arvore.value:
        return numero_existe(arvore.left, valor)
    else:
        return numero_existe(arvore.right, valor)

valor_remove = 5

print("Árvore antes da remoção:")
print(no)

if numero_existe(no, valor_remove):
    no = remove_numero(no, valor_remove)
    print(f"Árvore depois da remoção do número {valor_remove}:")
    print(no)
else:
    print(f"O número {valor_remove} não existe na árvore.")
