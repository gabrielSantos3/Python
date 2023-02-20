'''
Desafio 060

Faça um programa que leia um número qualquer e mostre o seu fatorial.
'''

'''
from math import factorial

n = int(input('Digite um número: '))
print(factorial(n))
'''
n = int(input('Digite um número: '))
r = 1
print(f'{n}! = ', end='')

while n > 0:
    print(n, end='')
    print(' x ' if n > 1 else ' = ', end='')
    r *= n
    n -=1
    
print(r, end='')