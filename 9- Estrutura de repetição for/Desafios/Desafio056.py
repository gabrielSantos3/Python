'''
Desafio 056

Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas e mostre:

-> A média de idade do grupo.
-> Qual é o nome do homem mais velho.
-> Quantas mulheres têm menos de 20 anos.
'''

somaIdade = 0
MediaIdade = 0
nomeVelho = ''
maiorIdadeHomem = 0
totMulher20 = 0

for i in range(1, 5):
    print(f'\n----- {i}ª PESSOA -----\n')
    
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).lower()[0]
    
    somaIdade += idade
    
    if i == 1 and sexo in 'm':
        maiorIdadeHomem = idade
        nomeVelho = nome
        
    if sexo in 'm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    
    if sexo in 'f' and idade < 20:
        totMulher20 += 1   
        
MediaIdade = (somaIdade / 4)

print('\n'+'-' * 21 + '\n')
print(f'A média de idade do grupo é: {MediaIdade:.2f} anos.\n')
print(f'O homem mais velho tem {maiorIdadeHomem} anos e se chama {nomeVelho}.\n')
print(f'Ao todo temos {totMulher20} mulher(es) abaixo de vinte anos.\n')