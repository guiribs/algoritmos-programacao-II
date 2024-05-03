# - Novos elementos sempre entram no 'topo' da pilha
# - O único elemento que se pode retirar da pilha em um dado momento é o elemento do topo
# Principais usos: modelagem de situações onde é preciso 'guardar para mais tarde' vários elementos e lembrar sempre do último elemento armazenado.
"""A cada comando call
- Empilha (push) o endereço para retornar depois
- Passa a executar a nova função
A cada comando return
- Desempilha (pop) o último endereço armazenado
- Passa a executar a partir do endereço desempilhado
Operações usuais:
- push(): empilha um elemento na pilha
- pop(): desempilha o elemento no topo da pilha
- top(): acessa o elemento do topo, sem desempilhá-lo
- empty(): verifica se a pilha está vazia"""

class Pilha():
    def __init__(self):
        self.data = []
        
    def push(self, x):
        self.data.append(x)
        
    def pop(self):
        if len(self.data) > 0:
            return self.data.pop(-1)
        
    def top(self):
        if len(self.data) > 0:
            return self.data[-1]
        
    def empty(self):
        return not len(self.data) > 0
    
p = Pilha()
num = 13

while num > 0:
    resto = num % 2
    num = num // 2
    p.push(resto)
    
while not p.empty():
    print(p.pop())