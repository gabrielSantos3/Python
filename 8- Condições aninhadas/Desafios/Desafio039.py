'''
Desafio 039

Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade: 

-> Se ele ainda vai se alistar no exército.
-> Se é a hora de se alistar
-> Se já passou do tempo de alistamento.

Seu programa também deve informar o tempo que falta ou passou do prazo. 
'''

from datetime import date

anoNascimento = int(input('Ano de Nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento

print(f'Quem nasceu em {anoNascimento} tem {idade} anos em {anoAtual}.')
if(idade < 18):
    print(f'Faltam {18 - idade} anos pra o alistamento.')
    print(f'Seu alistamento será em: {anoNascimento + 18}')
elif(idade > 18):
    print(f'O alistamento está atrasado em {idade - 18} anos.')
    print(f'Seu alistamento está atrasado desde: {anoNascimento + 18}')
else:
    print('Este ano é o ano de alistamento.')