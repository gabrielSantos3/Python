'''
Desafio 023

Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. 
'''

numero = int(input('Digite um número entre 0 e 9999: '))

print(f'Unidade: {numero // 1 % 10}')
print(f'Dezena: {numero // 10 % 10}')
print(f'Centena: {numero // 100 % 10}')
print(f'Milhar: {numero // 1000 % 10}')
