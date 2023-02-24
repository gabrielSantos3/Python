'''
Desafio 041

A confederação nacional de natação precisa de um programa que leia o ano de nascimento de
um atleta e mostre sua categoria, de acordo com a idade:

-> Até 9 anos: Mirim
-> Até 14 anos: Infantil
-> Até 19 anos: Júnior
-> Até 20 anos: Sênior
-> Acima: Master
'''

from datetime import date

actualYear = date.today().year
userYear = int(input('Em qual ano você nasceu? '))
age = actualYear - userYear

if(age < 10):
    print('Mirim')
elif(age < 15):
    print('Infantil')
elif(age < 20):
    print('Júnior')
elif(age < 21):
    print('Sênior')
else:
    print('Master')