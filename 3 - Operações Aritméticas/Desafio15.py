# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

print('=' * 70+'\nAluguel de carros\n'+'=' * 70)
d = int(input('Digite a quantidade de dias que o veículo foi alugado: '))
km = float(input('Digite a quantidade de Km rodados pelo veículo: '))
print('=' * 70)
print('Valor a ser pago pelo aluguel do veículo: ')
print(f'Valor do aluguel pela quantidade de dias: R$ {d * 60}')
print(f'Valor a ser pago pelos Km rodados: R$ {km * 0.15:.2f}')
print('=' * 70)
print(f'Total: R$ {(d*60) + (km * 0.15):.2f}\n\n')
