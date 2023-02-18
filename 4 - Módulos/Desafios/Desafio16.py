#crie um programa que receba um número real qualquer pelo teclado e mostre na tela sua porção inteira.
from math import trunc
n = float(input('Digite um número: '))
print(f'A parte inteira do número {n} é: {trunc(n)}')
m = float(input('Digite outro número: '))
print(f'A parte inteira do número {m} é: {int(m)}')