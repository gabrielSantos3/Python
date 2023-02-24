'''
Desafio 040

Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma
mensagem no final, de acordo com a média atingida. 

-> Média abaixo de 5.0: Reprovado
-> Média entre 5.0 e 6.9: Recuperação
-> Média igual ou superior a 7: Aprovado
'''

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
media = (n1 + n2) / 2

print(f'A média é de: {media :.2f}')

if(media < 5):
    print('Status: Reprovado.')
elif(media < 6.9):
    print('Status: Em Recuperação.')
else:
    print('Status: Aprovado.')