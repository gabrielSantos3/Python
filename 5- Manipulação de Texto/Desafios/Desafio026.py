'''
Desafio 026

Faça um programa que leia uma frase no teclado e mostre:

- Quantas vezes aparece a letra "A".
- Em que posição ela aparece pela primeira vez.
- Em que posição ela aparece na última vez.
'''

string = input('Digite algo: ').strip().lower()

lettersA = string.count('a')
print(f'\nA letra "A" aparece {lettersA} vezes.')

firstPosition = string.find('a')
lastPosition = string.rfind('a')
print(f'A primeira ocorrência dessa letra foi na posição: {firstPosition}')
print(f'A última ocorrência dessa letra foi na posição: {lastPosition}')
