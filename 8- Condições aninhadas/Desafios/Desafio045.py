'''
Desafio 045

Faça um programa que faça o computador jogar Jokenpo como usuário.
'''

from random import randint
from time import sleep

def line():
    print('*=' *  30 + '*\n')
    
def userWin():
    print('\nVocê venceu!')

def computerWin():
    print('\nO computador venceu!')
    

lista = ['Pedra', 'Papel', 'Tesoura']

line()
print('Pedra, Papel, Tesoura\n')
line()

print('Escolha uma opção: \n[0] Pedra \n[1] Papel \n[2] Tesoura\n')
user = int(input('Sua escolha: '))
print('\n')

if(user < 0 or user > 2):
    print('Opção Inválida!')
else:
    computer = randint(0, 2)
    
    line()
    print('\nJO...')
    sleep(1)
    print('KEN...')
    sleep(1)
    print('PO...')

    print(f'\nJogador jogou: {lista[user]}')
    print(f'Computador jogou: {lista[computer]}\n')
    
    if(user == 0 and computer == 1):
        computerWin()
    elif(user == 0 and computer == 2):
        userWin()
        
    elif(user == 1 and computer == 0):
        userWin()
    elif(user == 1 and computer == 2):
        computerWin()
        
    elif(user == 2 and computer == 0):
        computerWin()
    elif(user == 2 and computer == 1):
        userWin()
        
    else:
        print('Empate!')
    
    print()    
    line()