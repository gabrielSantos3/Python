'''
Desafio 042

Refaça o desafio 035 dos triângulos, desta vez acrescentando um recurso que tipo de 
triângulo será formado:

-> Equilátero: Todos os lados iguais
-> Isósceles: Dois lados iguais
-> Escaleno: Todos os lados diferentes
'''

r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

if(r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2):
    print('As retas podem formar um triângulo.')
    
    if(r1 == r2 and r2 == r3):
        print('Triângulo equilátero: Todos os lados iguais.\nÉ também Isósceles pois se possui três lados iguais, possui dois também.')
    elif(r1 == r2 or r2 == r3):
        print('Triângulo Isósceles. Dois lados iguais')
    else:
        print('Triângulo escaleno')
else:
    print('As retas não podem formar um triângulo.')