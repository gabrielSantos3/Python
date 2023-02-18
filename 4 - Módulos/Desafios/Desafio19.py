# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, recebendo o nome deles e escrevendo o nome do escolhido.
from random import choice

a = str(input('Digite o nome de um aluno: '))
b = str(input('Digite o nome de outro aluno: '))
c = str(input('Digite o nome de mais outro aluno: '))
d = str(input('Digite o nome do último aluno: '))

lista = [a, b, c, d]
cont = 0

while cont < 10:
    escolhido = choice(lista)
    print(f'O aluno escolhido para apagar o quadro foi: {escolhido}\n')
    cont += 1
