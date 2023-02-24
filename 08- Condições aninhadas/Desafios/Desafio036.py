'''
Desafio 036

Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado. 
'''

valorCasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salário mensal: '))
anos = float(input('Em quantos anos você deseja comprar a casa? '))

qtdMeses = 12 * anos
MaxSalario = 0.3 * salario * qtdMeses

if(valorCasa > MaxSalario):
    print('Netas condições, não é possível realizar o empréstimo.')
else:
    valorMensal = valorCasa / qtdMeses
    qtdParcelas = valorCasa / valorMensal
    
    print(f'A compra será dividida em: {round(qtdParcelas)} parcelas.')
    print(f'O valor mensal das parcelas será de: R${valorMensal :.2f}')
    