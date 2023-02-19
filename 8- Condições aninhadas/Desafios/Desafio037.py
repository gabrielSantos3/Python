'''
Desafio 037

Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão:

-> 1 para binário
-> 2 para octal
-> 3 para hexadecimal
'''

n = int(input('Digite um número inteiro: '))
print('\nEscolha uma das bases de conversão: \n\n[1] Binário\n[2] Octal\n[3] Hexadecimal\n')

c = int(input('Sua opção: '))

if(c == 1):
    print(f'{n} convertido para BINÁRIO é: {bin(n)[2:]}')
elif(c == 2):
    print(f'{n} convertido para OCTAL é: {oct(n)[2:]}')
elif(c ==3):
    print(f'{n} convertido para HEXADECIMAL é: {hex(n)[2:]}')
else:
    print('Opção Inválida!')