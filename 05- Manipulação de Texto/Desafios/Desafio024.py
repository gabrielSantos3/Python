'''
Desafio 024

Crie um programa que leia  o nome de uma cidade e diga se ela começa ou não com o nome "Santo". 
'''

cityName = input('Digite o nome da sua cidade: ').strip().lower()
cityName = cityName.split(' ')

if (cityName[0] == 'santo'):
    print('Sua cidade começa com "Santo".')
else:
    print('Sua cidade não começa com "Santo."')