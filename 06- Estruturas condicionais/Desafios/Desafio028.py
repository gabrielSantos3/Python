'''
Desafio 028

Escreva um programa que sorteie um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido. Em seguida, deve imprimir na tela se o usuário venceu ou não.
'''

from random import randint
from time import sleep

def line():
    print('*=' * 30 + '*\n')
    
line()
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!\n')
line()

random = randint(0, 5)
input = int(input('Em qual número eu pensei? '))

print('PROCESSANDO...')
sleep(2)

if(input < 0 or input > 5):
    print('Digite um número válido!')
else:
    if(random == input):
        print(f'Você venceu! O número escolhido foi: {random}')
    else:
        print(f'Você perdeu! O número escolhido foi: {random}')
