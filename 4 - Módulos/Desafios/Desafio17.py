#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo e mostre o valor de sua hipotenusa

from math import hypot

co = int(input('Digite o valor do cateto oposto do triângulo: '))
ca = int(input('Digite o valor do cateto adjacente do triângulo: '))

'''
qc = pow(co, 2) + pow(ca,2)
print(f'O valor da hipotenusa é: {sqrt(qc):.2f}')
'''
print(f'O valor da hipotenusa é: {hypot(ca,co):.2f}')
