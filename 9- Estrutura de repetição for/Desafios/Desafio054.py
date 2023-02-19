'''
Desafio 054

Crie um programa que leia o ano de nascimento de 7 pessoas e imprima, no final, quantas
são maiores de idade e quantas são menores.
'''

from datetime import date

maior = 0
menor = 0
year = 0
actualYear = date.today().year

for i in range(7):
    year = int(input('Ano de Nascimento: '))
    
    if(actualYear - year > 18):
        maior += 1
    else:
        menor += 1
        
print(f'\n{maior} pessoas maiores de idade.')
print(f'{menor} pessoas menores de idade.\n')