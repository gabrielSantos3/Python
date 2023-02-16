#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere: US$ 1,00 = R$5,41.

d = float(input('Quantos reais você tem na carteira? R$'))
print('Você pode comprar US${:.2f} com esse valor.'.format(d/5.41))