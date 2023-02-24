'''
Desafio 046

Faça um programa que mostre na tela a contagem regressiva para um estouro de fogos de 
artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''

from time import sleep

print('A contagem vai começar:\n')
sleep(1)

for i in range(10, 0, -1):
    print(f'{i}...')
    sleep(1)
    
print('\nFim!!')