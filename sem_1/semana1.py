"""#int, float, bool, str e complex são imutáveis, ou seja, alocado uma vez na memória não irá se alterar, mas sim criar um novo objeto
d = 10
e = 10.2
f = "Texto"
g = True
h = complex

#listas são mutáveis
a = [1,2,3]
b = a
print(b)
b[1] = 0
print(b , a)

#O valor não se altera, pois int é imutável
def g(x):
    x = 5
c = 2
g(c)
print(c)

#O valor se altera, pois lista é mutável
def h(lst):
    lst[0] = 1
myList = [0,1,2,3]
h(myList)
print(myList)

#Função para abrir arquivo
open('text.txt', 'r')  #Leitura
open('text.txt', 'w')  #Escrita
open('text.txt', 'a')  #Escrita no final do arquivo
open('text.txt', 'r+') #Leitura e escrita
#open('text.txt', 't')  #Modo texto (padrão)
#open('text.txt', 'b')  #Modo binario
arquivo = open('text.txt')
#arquivo.read(n)
arquivo.read()
arquivo.readline()
arquivo.readlines()
#arquivo.write(n)
arquivo.close() #Fechar arquivo

#Exemplo de abertura e manipulados de dados do arquivo
def readFile(filename):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    wordList = content.split()  #Dividir por token ou palavras, usando a função split para criar uma lista
    print(wordList)
    return len(wordList), len(content)
                              
n_words, n_chars = readFile('teste.txt')
print(n_words, n_chars)

#Escrevendo no arquivo
outfile = open('teste2.txt', 'w')
outfile.write('Sobre escrevi o texto!\n')
idade = 30
outfile.write('Minha idade é' + str(idade) + 'anos.\n')
outfile.write('Minha idade é {} anos.\n'.format(idade))

#Ex. 3.14 - trocar o valor do primeiro com o ultimo item da lista
def trocaPU(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
ingredientes = ['farinha', 'açúcar', 'manteiga', 'maçãs']
trocaPU(ingredientes)
print(ingredientes)

#Aprendendo a usar o modulo turtle
import turtle
help(turtle.Turtle)
s = turtle.Screen()
t = turtle.Turtle()
t.forward(100)
t.left(90)
t.pensize(20)
t.circle(100)
u = turtle.Turtle()
u.left(90)
u.forward(100)
t.forward(100)
u.right(45)

#Ex. 3.15 - Desenhar simbolo olimpiadas
import turtle
s = turtle.Screen()
t = turtle.Turtle()

def olimpíadas(t):
    for i in range(5):
        color = ['blue', 'black', 'red', 'yellow', 'green']
        x = [-110, 0, 110, -55, 55]
        y = [0, 0, 0, -50, -50]

        t.teleport(x[i], y[i])
        t.pencolor(color[i])
        t.pensize(4)
        t.circle(50)

olimpíadas(t)


#Ex. 4.8
def palavras1(arq):
    infile = open(arq, 'r')
    content = infile.read()
    infile.close()
    tabela = str.maketrans('!,.:;?@#$%¨&*()', 15*' ')
    content = content.translate(tabela)
    content = content.lower()
    return content.split()
    
    
def palavras(nomearq):

    'retorna a lista de palavras reais, sem pontuação'
    arqEntrada = open(nomearq, 'r')
    conteúdo = arqEntrada.read()
    arqEntrada.close()
    tabela = str.maketrans('!,.:;?', 6*' ')
    conteúdo=conteúdo.translate(tabela)
    conteúdo=conteúdo.lower()
    return conteúdo.split()

arquivo = 'example.txt'
print(palavras(arquivo))
print(palavras1(arquivo))

#Código ChatGPT:
import re

def palavras(nome_arquivo):
    # Abre o arquivo para leitura
    with open(nome_arquivo, 'r') as arquivo:
        # Lê o conteúdo do arquivo
        texto = arquivo.read()
        
        # Usa expressão regular para encontrar todas as palavras no texto
        palavras = re.findall(r'\b\w+\b', texto)
        
        # Retorna a lista de palavras
        return palavras

# Exemplo de uso da função
nome_arquivo = 'example.txt'  # Substitua 'texto.txt' pelo nome do seu arquivo
lista_palavras = palavras(nome_arquivo)
print(lista_palavras)
"""

#Ex. 4.9
def meuGrep1(arq, find_Word):
    infile = open(arq, 'r')
    for linha in infile:
        if find_Word in linha:
            print(linha, end = '')  
#meuGrep('example2.txt', 'line')

def meuGrep(nomearq, alvo):

    'exibe cada linha do arquivo que contém a string alvo'
    arqEntrada = open(nomearq)
    for linha in arqEntrada:
        if alvo in linha:
           print(linha, end='')
           
meuGrep('example2.txt', 'line')

#Ex. 4.10