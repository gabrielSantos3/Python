'''
Desafio 048

Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3
e que se encontram no intervalo de 1 até 500.
'''

sum = 0
cont = 0

for i in range(3, 499, 2):
    if(i % 3 == 0):
        sum += i
        cont += 1
    
print(f'A soma dos {cont} valores é: {sum}')