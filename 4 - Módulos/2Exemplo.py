from math import ceil, sqrt, floor

a = ceil(7.89) #arredonda para cima
b = floor(7.89) #arredonda para baixo
c = sqrt(144) #calcula a raíz quadrada
print(f'Ceil: {a} / Floor: {b} / SQRT: {c}')

raiz = int(input('Digite um número para calcular raíz quadrada: '))
print(f'A raíz é: {floor(sqrt(raiz))}') #Calcula a raíz e aproxima para o número mais baixo