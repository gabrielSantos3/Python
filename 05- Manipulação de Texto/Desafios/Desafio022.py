'''
Desafio 022

Crie um programa que leia o nome completo de uma pessoa e mostre: 
 - O nome com todas as letras maiúsculas.
 - O nome com todas as letras minúsculas.
 - Quantas letras possui (sem considerar os espaços)
 - Quantas letras tem o primeiro nome.
'''

nome = input('Digite seu nome: ')
print('Maiúsculo: ' +nome.upper())
print('Minúsculo: ' +nome.lower())

lista = nome.split(' ') # Separa a string
listaJoin = ''.join(lista) # Junta novamente sem espaços
print(f'O nome possui: {len(listaJoin)} letras.')

print(f'Seu primeiro nome é: {lista[0]} e possui: {len(lista[0])} letras.')


