'''
Desafio 059

Crie um programa que leia dois valores e mostre um menu na tela.

[1] Somar 
[2] Multiplicar
[3] Maior
[4] Escolher novos números
[5] Sair

Seu programa deve realizar a operação solicitada em cada caso.
'''

from time import sleep

def line():
    print('\n' + '*=' * 30 + '*\n')

a = float(input('\nPrimeiro valor: '))
b = float(input('Segundo valor: '))

option = 0

print()

while option != 5:
    
    
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Escolher novos números
[5] Sair\n''')
    
    option = int(input('Sua opção: '))
    print()
    
    if option < 1 or option > 5:
        print('Valor inválido. Tente novamente.\n')
    
    match option:
        case 1:
            result = a + b
            print(f'A soma entre {a} e {b} é {result}')
            line()
            
        case 2:
            result = a * b
            print(f'A multiplicação de {a} por {b} é {result}')
            line()
        
        case 3:
            if(a > b):
                result = a
            elif(a < b):
                result = b
            else:
                result = 0
            
            if(result == 0):
                print('Os dois valores são iguais.')
            else:    
                print(f'O maior número entre {a} e {b} é {result}')
                
            line()
          
        case 4:
            a = float(input('\nNovo primeiro valor: '))
            b = float(input('Novo segundo valor: '))  
            
            line()
        case 5:
            print('SAINDO...')
            sleep(2)
            print()