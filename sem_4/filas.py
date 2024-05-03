# Definição: estrutura para armazenar um conjunto de elementos, que funciona da seguinte forma:
# - Novos elementos sempre entram no fim da fila
# - O único elemento que pode ser retirado da fila, em um determinado momento, é seu primeiro elemento
"""Operações usuais:
- inserir(): insere um elemento no fim da fila
- remover(): remove o primeiro elemento da fila
- empty(): verifica se a fila está vazia"""

class Fila():
    def __init__(self):
        self.data = []
    
    def inserir(self, x):
        self.data.append(x)
        
    def remover(self):
        if len(self.data) > 0:
            return self.data.pop(0)
        
    def top(self):
        if len(self.data) > 0:
            return self.data[0]
        
    def empty(self):
        return not len(self.data) > 0
    
"""Implementar um programa de gerenciamento
de duas filas em um banco: prioritária e
normal.
Seu programa deverá permitir que pessoas
sejam inseridas no fim de cada fila,
dependendo da idade de cada uma (acima de
60 anos entra na fila prioritária).
A saída de pessoas da fila deve ocorrer da
seguinte forma: a cada duas pessoas que
saem da fila prioritária, uma sai da fila normal."""

p = Fila()
n = Fila()

pessoas = [10, 100, 30, 50, 60, 65, 20, 70, 15, 75, 5]

for idade in pessoas:
    if idade > 60:
        p.inserir(idade)
    else:
        n.inserir(idade)
        
while not p.empty() or not n.empty():
    for _ in range(2):
        if not p.empty():
            print(p.remover())
    if not n.empty():
        print(n.remover())
    