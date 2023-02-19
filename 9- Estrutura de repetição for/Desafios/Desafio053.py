'''
Desafio 053

Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
desconsiderando os espaços.

'''

text = str(input('Digite alguma coisa: '))
reverse = ''

text = text.lower().split()
text = ''.join(text)
        
for i in range(len(text) - 1, -1, -1):
    reverse += text[i]

print(f'\nO inverso de {text} é: {reverse}')    
if(reverse == text):
    print('Temos um Palíndromo!')
else:
    print('A frase digitada não é Palíndromo.')