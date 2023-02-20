'''
Desafio 063

Escreva um programa que leia um número inteiro n e mostre na tela os n primeiros elementos da sequência de Fibonacci.
'''

num = int(input('\nQuantos elementos da sequência você deseja ver? '))
seq = [1, 1]
cont = 2

'''
for i in range(2, num):
    el = seq[i-1] + seq[i-2]
    seq.append(el)
    
print(seq)
'''
if num == 1:
    print(f'\n[{seq[0]}]\n')
    exit(0)
elif(num == 2):
    print(f'\n{seq}\n')
    exit(0)
while cont < num:    
    el = seq[cont-1] + seq[cont-2]
    seq.append(el)
    
    cont += 1

print()
print(seq)
print()