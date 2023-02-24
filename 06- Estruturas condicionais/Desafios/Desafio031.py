'''
Desafio 031

Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 para viagens de até 200 km e R$ 0,45 para viagens mais longas.
'''

viagem = float(input('Qual a distância da viagem que você planeja fazer? '))

if(viagem > 200):
    print(f'O custo da viagem será de: R${viagem * 0.45 :.2f}')
else:
    print(f'O custo da viagem será de: R${viagem * 0.5 :.2f}')