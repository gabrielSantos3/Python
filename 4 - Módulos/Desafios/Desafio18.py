#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

a = int(input('Digite o valor de um ângulo qualquer: '))
print(f'Seno de {a}°: {math.sin(math.radians(a)):.2f}')
print(f'Cosseno de {a}°: {math.cos(math.radians(a)):.2f}')
print(f'Tangente de {a}°: {math.tan(math.radians(a)):.2f}')