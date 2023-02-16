#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Digite o valor atual do seu salário, em reais: '))
print('O valor do seu novo salário será de: R$ {:.2f}'.format(s * 1.15))