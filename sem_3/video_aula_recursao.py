"""def imprime(l):
    for i in range(len(l)):
        print(l[i])
        
def imprime_recursao(l, i = 0):
    if i < len(l):
        print(l[i])
        imprime_recursao(l, i+1)
        
lista = [1, 2, 3, 4]

imprime(lista)
imprime_recursao(lista)

def cal_fatorial(n): 
    if n == 0:
        return 1
    else:
        res = n * cal_fatorial(n-1)
        return res
        
print(cal_fatorial(1))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = 10
print("Sequência de Fibonacci até o", n, "º termo:")
for i in range(n):
    print(fibonacci(i), end=" ")
    
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Exemplo de uso
n = 11
print("Sequência de Fibonacci até o", n, "º termo:")
for i in range(n):
    print(fibonacci(i), end=" ")

def f(n): 
    if n < 2: 
        return n 
    else: 
        return f(n-1) + f(n-2) 
 
print(f(6)) """

def f(v, i): 
    if i == 0: 
        return v[i] 
    else: 
        return min(v[i], f(v, i - 1)) 
 
l = [5,4,6,8,10,12] 
print(f(l, len(l) - 1)) 