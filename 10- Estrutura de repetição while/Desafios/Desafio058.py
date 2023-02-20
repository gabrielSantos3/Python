'''
Desafio 058

Melhore o jogo do desafio 028 onde o computador vai 'pensar' em um número entre 1 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantas
tentativas foram necessárias para o jogador vencer.
'''

from random import randint
from time import sleep

def line():
    print('*=' * 30 + '*\n')
    
    
computador = randint(1, 10)

line()
print('Vou pensar em um número entre 1 e 10. Tente adivinhar!\n')
line()

acertou = False
cont = 0

while not acertou:  
    cont += 1   
    jogador = int(input('Em qual número eu pensei? '))
    
    print('\nPROCESSANDO...\n')
    sleep(2)

    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Menos... tente novamente.\n')
        else:
            print('Mais... tente novamente.\n')

    line()
print(f'Você venceu! O número sorteado foi {computador}.\n')
print(f'Foram necessárias {cont} tentativas.\n')