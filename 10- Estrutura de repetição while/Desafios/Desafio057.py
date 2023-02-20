'''
Desafio 057

Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'. Caso
esteja errado, peça a digitação novamente até ter um valor correto.
'''

sexo = str(input('Sexo: [M / F]: ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Valor inválido. Informe seu sexo novamente: [M / F]: '))


print(f'Sexo Masculino registrado com sucesso.' if sexo in 'mM' else 'Sexo Feminino registrado com sucesso.')