# Algoritmos de Busca - ordenar a lista primeiro

# Busca Linear

# Com o in:
l = [7, 6, 3, 4]
3 in l
8 in l

# Com o index():
l.index(3)
# l.index(5)

"""Teremos 3 possibilidades:
- l[i] == elemento desejado à finaliza a busca
- l[i] > elemento desejado à elemento pode
estar à esquerda
- l[i] < elemento desejado à elemento pode
estar à direita"""

def busca_binaria(l, x, inicio, fim):
    meio = (inicio + fim) // 2
    
    if fim < inicio:
        return -1
    elif x == l[meio]:
        return meio
    elif x < l[meio]:
        return busca_binaria(l, x, inicio, meio - 1)
    elif x > l[meio]:
        return busca_binaria(l, x, meio + 1, fim)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(busca_binaria(lista, 11, 0, len(lista)))