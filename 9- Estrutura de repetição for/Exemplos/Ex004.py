print('Os números pares entre 0 e 20 são: ')

for i in range(0, 20, 2):
    print(i, end=' - ') # imprime na mesma linha dando um espaço no final
    
print('\n\nOs números ímpares entre 0 e 20 são: ')

for i in range(1, 20, 2):
    print(i, end=' ')