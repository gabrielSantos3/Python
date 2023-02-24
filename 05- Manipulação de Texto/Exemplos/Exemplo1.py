# Manipulação de Strings

nome = "Trabalhando com strings"

print(f'O tamanho da string é: {len(nome)}')

print(nome.find('strings'))

novoNome = nome.replace('strings', 'string')
print(novoNome)

listaNome = nome.split(' ')
print(listaNome)

print(nome.upper())

print(nome.lower())


# 1 - Fatiamento

print(nome[0:23:2])

print(nome[:11])

print(nome[12:])

print(nome.count('a'))

print('com' in nome)

nome = 'I Love Python'
print(nome.capitalize())

nome = 'i love python'
print(nome.title())

nome = '   i love python  '
print(nome.strip(), nome.rstrip(), nome.lstrip())

texto = ['Eu', 'amo', 'Python']
print(' '.join(texto))

print("""Eu estou escrevendo aqui um texto bem grande. \nÉ recomendado que para estes casos, se use as três aspas para delimitar a string. """)