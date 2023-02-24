from random import choice
from time import sleep

lista = ['Banana', 'Cereja', 'limão']
f1 = ''
f2 = ''
f3 = ''

r = int(input('Quantas rodadas você deseja jogar? '))

for i in range(0, r):
    f1 = choice(lista)
    f2 = choice(lista)
    f3 = choice(lista)
    
    sleep(1)
    print()
    
    print(f1, end=' - ')
    print(f2, end=' - ')
    print(f3)
    
    if(f1 == f2 and f2 == f3):
        print('\nParabéns! Você venceu!\n')
        exit(0)

    sleep(1)