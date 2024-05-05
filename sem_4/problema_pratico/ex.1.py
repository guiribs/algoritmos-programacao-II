#  Escreva um programa que leia do teclado dois conjuntos de nomes de frutas. Em seguida, apresente na tela a união (operador | ), a interseção (&) e a diferença simétrica (^). Utilizando a função len, verifique qual dos conjuntos tem mais elementos e apresente a diferença entre o maior e o menor (–).

def main():
    # Leitura dos conjuntos de frutas do teclado
    conjunto1 = set(input("Digite os nomes das frutas do primeiro conjunto, separados por espaço: ").split())
    conjunto2 = set(input("Digite os nomes das frutas do segundo conjunto, separados por espaço: ").split())

    # Apresenta na tela a união, interseção e diferença simétrica
    print("União dos conjuntos:", conjunto1 | conjunto2)
    print("Interseção dos conjuntos:", conjunto1 & conjunto2)
    print("Diferença simétrica dos conjuntos:", conjunto1 ^ conjunto2)

    # Verifica qual conjunto tem mais elementos e apresenta a diferença entre o maior e o menor
    if len(conjunto1) > len(conjunto2):
        diferenca = len(conjunto1) - len(conjunto2)
        print("O conjunto 1 tem mais elementos do que o conjunto 2.")
        print("A diferença entre o número de elementos do conjunto 1 e o conjunto 2 é:", diferenca)
    elif len(conjunto2) > len(conjunto1):
        diferenca = len(conjunto2) - len(conjunto1)
        print("O conjunto 2 tem mais elementos do que o conjunto 1.")
        print("A diferença entre o número de elementos do conjunto 2 e o conjunto 1 é:", diferenca)
    else:
        print("Os conjuntos têm o mesmo número de elementos.")


if __name__ == "__main__":
    main()
