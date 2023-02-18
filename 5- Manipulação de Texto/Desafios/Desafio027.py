'''
Desafio 027

Faça um programa que leia o nome completo de uma pessoa e mostre o primeiro e o último nome separadamente.
'''

userName = input('Digite seu nome completo: ').strip()
userName = userName.split(' ')

print(f'\nPrimeiro nome: {userName[0]}')
print(f'Último nome: {userName[len(userName) - 1]}')