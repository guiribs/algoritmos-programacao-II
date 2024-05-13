# Merge sort: dividir para conquistar
# dividi em duas partes, e mais duas partes, e mais duas partes...

def intercala(v, ini, meio, fim):
    L = v[ini:meio+1]
    R = v[meio+1:fim+1]
    L.append(999) #sentinela
    R.append(999) #sentinela
    i = 0
    j = 0
    for k in range(ini, fim+1):
        if L[i] <= R[j]:
            v[k] = L[i]
            i += 1
        else:
            v[k] = R[j]
            j += 1

def merge_sort(v, ini, fim):
    if ini < fim:
        meio = (ini + fim) // 2
        merge_sort(v, ini, meio)
        merge_sort(v, meio+1, fim)
        intercala(v, ini, meio, fim)
    return v;
        
lista_desordenada = [9, 7, 5, 3, 1, 8, 6, 4, 2, 0]
lista_ordenada_merge_sort = merge_sort(lista_desordenada, 0, len(lista_desordenada)-1)
print(lista_ordenada_merge_sort)


# Quick sort: dividir para conquistar, dividir em dois menores, elemento pivo = x, esquerda menor ou igual a x, direita maior ou igual a x.

# Escolha de um elemento pivô x, colocando-o em sua posição correta - Ordenar de forma que os elementos à esquerda do pivô são menores ou iguais a ele e os elementos à direita são maiores ou iguais a ele - Percorrer o vetor v da esquerda para direita até v[i] >= x; e da direita para esquerda até que v[j] <= x. - Trocar v[i] com v[j], incrementar i, decrementar j - Quando i e j se cruzarem, a iteração finaliza, de forma que v[0]...v[j] são menores ou iguais a x e v[i]...v[n-1] são maiores ou iguais a x

vetor_desordenado = [25, 33, 35, 12, 37, 86, 92, 57]

def quick_sort(v, ini, fim):
    meio = (ini + fim) // 2
    pivo = v[meio]
    i = ini
    j = fim
    while i < j:
        while v[i] < pivo:
            i += 1
        while v[j] > pivo:
            j -= 1
        if i <= j:
            v[i], v[j] = v[j], v[i]
        i += 1
        j -= 1
    if j > ini:
        quick_sort(v, ini, j)
    if i < fim:
        quick_sort(v, i, fim)