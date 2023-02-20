'''
Desafio 062

Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
'''

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
print()
cont = 1
limite = 11

while cont != limite:
    print(a1, end=' ')
    a1 += r
    cont += 1
    
mais = int(input('\n\nDigite quantos termos a mais você deseja exibir: '))
print()
cont = 0
limite = mais    

while cont != limite:
    print(a1, end=' ')
    a1 += r
    cont += 1
    
print('\n')