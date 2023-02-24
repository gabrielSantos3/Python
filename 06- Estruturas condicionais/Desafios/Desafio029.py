'''
Desafio 029

Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada quilômetro acima do limite.
'''

speed = int(input('Digite a velocidade do carro: '))

if(speed > 80):
    print(f'Você ultrapassou o limite. A multa será de R${(speed - 80) * 7},00.')
else:
    print('Velocidade permitida.')