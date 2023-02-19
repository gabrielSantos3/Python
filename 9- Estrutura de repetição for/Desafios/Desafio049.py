'''
Desafio 049

Refaça o desafio 009 (tabuada) mas desta vez usando o laço de repetição for.
'''

num = int(input('Número da tabuada: '))

for i in range(11):
    print(f'{i} X {num} = {i * num}')