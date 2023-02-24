'''
Desafio 025

Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
'''

name = input('Digite seu nome completo: ').strip().lower()
haveSilva = 'silva' in name

if(haveSilva):
    print('Você possui Silva em seu nome.')
else:
    print('Você não possui Silva em seu nome.')