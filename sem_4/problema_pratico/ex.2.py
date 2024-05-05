# Altere o programa do Exercício resolvido 6.2 da seguinte maneira: leia um número inteiro N (N < 30) e faça que o conjunto A tenha tamanho N e o conjunto B tenha tamanho 30-N.
# LivroPython3

"""from random import randint

A = set()
while len(A) < 15:
    A.add(randint(1, 30))
B = set(range(1, 31)) - A
print("Conjunto A: {}".format(A))
print("Conjunto B: {}".format(B))
print("\nFim do programa")"""

from random import randint

try:
    N = int(input("Digite um número inteiro N (N < 30): "))
    if N >= 30:
        print("Erro: N deve ser menor que 30.")
        exit()

    A = set()
    while len(A) < N:
        A.add(randint(1, 30))

    B = set(range(1, 31)) - A

    print("Conjunto A: {}".format(A))
    print("Conjunto B: {}".format(B))
    print("\nFim do programa")
except ValueError:
    print("Erro: Você deve digitar um número inteiro.")