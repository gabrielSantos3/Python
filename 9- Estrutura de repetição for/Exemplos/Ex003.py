name = str(input('Digite um nome qualquer: '))
inverse = ''

for i in range(len(name) - 1, -1, -1):
    inverse += name[i]
    
if(name == inverse):
    print(f'A palavra {name} é um Palíndromo!')
else:
    print(f'A palavra {name} não é um Palíndromo!')    
