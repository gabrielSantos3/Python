'''
Desafio 033

Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))

menor = a
maior = a

if(b < a and b < c):
    menor = b
    
if(c < a and c < b):
    menor = c
    
if(b > a and b > c):
    maior = b
    
if(c > a and c > b):
    maior = c
    

    
print(f'O maior número é: {maior}, e o menor é: {menor}.')