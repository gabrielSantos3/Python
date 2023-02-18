'''
Desafio 032

Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''

from datetime import date

year = int(input('Digite um ano qualquer, ou 0 para o ano atual: '))

if(year == 0):
    year = date.today().year

if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print(f'O ano {year} é bissexto.')
else:
    print(f'O ano {year} não é bissexto.')