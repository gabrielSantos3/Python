'''
Desafio 055

Faça um programa que leia o peso de 5 pessoas. No final, mostre quais foram o maior e o 
menor peso lidos.
'''

weight = 0.0
menor = 0
maior = 0

for i in range(5):
    weight = float(input('Seu peso: '))
    
    if(i == 0):
        menor = weight
        maior = weight
    
    else:
        if(weight > maior):
            maior = weight
        if(weight < menor):
            menor = weight
        
print(f'O maior peso registrado foi: {maior} Kg')
print(f'O menor peso registrado foi: {menor} Kg')