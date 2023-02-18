'''
Desafio 034

Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1250,00 o aumento será de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''

wage = float(input('Digite o valor do salário: '))
up = 0

if(wage > 1250):
    up = wage * 0.1
    print(f'O aumento é de 10%, equivalente a: R${up:.2f}')
    print(f'O novo salário será: R${wage + up :.2f}')
else:
    up = wage * 0.15
    print(f'O aumento é de 15%, equivalente a: R${up:.2f}')
    print(f'O novo salário será: R${wage + up :.2f}')
