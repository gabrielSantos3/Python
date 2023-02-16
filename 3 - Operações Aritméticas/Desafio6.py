#Desenvolva um programa que receba um número inteiro e mostre seu dobro, triplo e raíz quadrada.

num = int(input('Digite um número qualquer: '))

print('O dobro de {} é {}, seu triplo é {}, e sua raiz quadrada, {:.2f}'.format(num, 2*num, 3*num, pow(num,(1/2))))