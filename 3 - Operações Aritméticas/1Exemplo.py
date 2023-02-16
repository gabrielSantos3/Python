'''
Ordem de precedência nas operações em Python
1 - Parênteses ()
2 - Potências (**)
3 - Multiplicação (*) | divisão (/) | divisão inteira (//) | resto da divisão (%)
4 - Adição (+) | subtração (-)

Há ainda os operadores que podem ser usados em strings
Concatenação (+)
Multiplicação (*)
'''

nome = input('Digite seu nome: ')

print('\nOlá, {:20}!\n'.format(nome))  #O nome será mostrado em um espaço de vinte caracteres com o alinhamento padrão (à esquerda)

print('Olá, {:<20}!\n'.format(nome))  #O nome será mostrado em um espaço de vinte caracteres com o alinhamento à esquerda

print('Olá, {:>20}!\n'.format(nome))  #O nome será mostrado em um espaço de vinte caracteres com o alinhamento à direita

print('Olá, {:^20}!\n'.format(nome))  #O nome será mostrado em um espaço de vinte caracteres com o alinhamento centralizado

print('Olá, {:=^20}!\n'.format(nome))  #O nome será mostrado em um espaço de vinte caracteres com o alinhamento centralizado e preenchido com o símbolo de igual nos espaços sobrando

print('Olá, {:*^20}!\n'.format(nome))  #O nome será mostrado em um espaço de vinte caracteres com o alinhamento centralizado e preenchido com o símbolo de asterisco nos espaços sobrando
