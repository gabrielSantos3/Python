'''
Desafio 35

Desenvolva um programa que leia o cumprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''

r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

if(r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2):
    print('As retas podem formar um triângulo.')
else:
    print('As retas não podem formar um triângulo.')