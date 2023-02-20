'''
Desafio 065

Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores digitados e quais foram o menor e o maior número.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

media = 0.0
menor = maior = cont  = soma = 0
sair = False

while not sair:
    num = int(input('Digite um número: '))
    resp = str(input('Deseja acrescentar mais um número?[S/N] ')).strip().lower()[0]
    
    print()
    
    if resp == 'n':
        sair = True

    cont +=1
    soma += num
    
    if cont == 1:
        menor = maior = num
        
    else:
        if(num > maior):
            maior = num
        if(num < menor):
            menor = num
    
media = soma / cont

print(f'A média entre todos os valores digitados é: {media :.2f}')
print(f'O maior número registrado foi: {maior}')
print(f'O menor número registrado foi: {menor}')

    
