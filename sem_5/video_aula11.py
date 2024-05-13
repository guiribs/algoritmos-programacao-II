# sort()

lista = [9,4,5,2,6,7,8,6]
lista2 = [9,4,5,2,6,7,8,6]
listanova = lista2.sort()
print("Lista nova:", listanova)

lista_ordenada = sorted(lista)

print(lista_ordenada)

# Ordenação interna vs. externa: cabe na memoria principal vs. não cabe e armazena em disco

# Ordenação estável: se for igual, ordena na ordem de registro

# Bubble sort: percorre varias vezes, compara cada elemento com o seu sucessor, e troca caso esteja na ordem incorreta, são feitas n-1 iterações

def bubble_sort(v):
    for i in range(len(v)-1):
        for j in range(len(v)-i-1):
            if (v[j] > v[j+1]):
                v[j], v[j+1] = v[j+1], v[j]
    return v;

def insertion_sort(v):
    for i in range(1, len(v)):
        x = v[i]
        j = i-1
        while j >= 0 and x < v[j]:
            v[j+1] = v[j]
            j -= 1
        v[j+1] = x
    return v;

lista_desordenada = [97, 43, 52, 23, 64, 72, 84, 63, 83, 4]

lista_ordenada_bubble_sort = bubble_sort(lista_desordenada)
print(lista_ordenada_bubble_sort)

lista_ordenada_insertion_sort = insertion_sort(lista_desordenada)
print(lista_ordenada_insertion_sort)