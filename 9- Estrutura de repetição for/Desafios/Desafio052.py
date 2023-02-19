'''
Desafio 052

Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

def isPrime(num): 
    
    if(num == 0 or num == 1):
        return False
    else:
        for i in range(2, num):
            if(num % i == 0):
                return False

    return True
    
    
    
    
num = int(input('Digite um número inteiro: '))

if(isPrime(num) == True):
    print(f'O número {num} é primo.')
else:
    print(f'O número {num} não é primo.')
