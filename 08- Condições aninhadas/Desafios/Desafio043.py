'''
Desafio 043

Desenvolva um programa que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre
seu status, de acordo com as informações abaixo

-> Abaixo de 18.5: Abaixo do peso
-> Entre 18.5 e 25: Peso normal
-> 25 até 30: Sobrepeso
-> 30 até 40: Obesidade
-> Acima de 40: Obesidade mórbida
'''

weight = float(input('\nDigite o seu peso: '))
height = float(input('Digite a sua altura: '))

if(weight <= 0 or height <= 0):
    print('Insira os dados corretamente e tente de novo.')
else:
    imc = weight / (height ** 2)

    print(f'O valor do seu IMC é: {imc :.2f}')

    if(imc < 18.5):
        print('Você está abaixo do peso.')
    elif(imc < 25):
        print('Peso normal')
    elif(imc < 30):
        print('Sobrepeso')
    elif(imc < 40):
        print('Você está obeso.')
    else:
        print('Obesidade mórbida.')