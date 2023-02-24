'''
Desafio 050

Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
que forem pares. Desconsidere os que forem ímpares.
'''
num = 0
sum = 0

for i in range(6):
    num = int(input('Digite um número inteiro: '))
    
    if(num%2 == 0):
        sum += num

print(f'A soma dos números pares é: {sum}')