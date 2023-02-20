'''
Desafio 061

Refaça o desafio 051, lendo o primeiro termo e a razão de uma P.A., mostrando os dez
primeiros termos da progressão usando a estrutura while.
'''

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 1

#for i in range(a1, a1 + 10):
while cont != 11:
    print(a1, end=' ')
    a1+= r
    cont += 1
    