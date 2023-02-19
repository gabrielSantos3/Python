'''
Desafio 051

Desenvolva um programa que leia o primeiro termo e a razão de uma P.A.  e no final
mostre os dez primeiros termos dessa progressão.
'''

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

for i in range(a1, a1 + 10):
    print(a1, end=' ')
    a1+= r
    