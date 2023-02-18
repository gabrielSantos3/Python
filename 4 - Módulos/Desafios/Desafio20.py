#Um professor deseja sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle

a = str(input('Digite um nome: '))
b = str(input('Digite um nome: '))
c = str(input('Digite um nome: '))
d = str(input('Digite um nome: '))

lista = [a, b, c, d]
cont = 0
while cont < 10:
    shuffle(lista)
    print('A ordem de apresentação será: ')
    print(lista)
    cont+=1
    #Aparentemente pode ser sorteada a mesma ordem inicial