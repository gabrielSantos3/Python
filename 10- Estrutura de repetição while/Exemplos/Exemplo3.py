from random import choice

lista = ['chão', 'buraco']
newLista = ['chão']
moveLista = []
position = 0

for i in range(9):
    newLista.append(choice(lista))
   
newLista.append('Maçã') 
print(f'\n{newLista}\n')

while position < 11:
    prox = newLista[position]
    
    if prox == 'chão':
        moveLista.append('andar')
        
    elif(prox == 'buraco'):
        moveLista.append('pular')
    
    else:
        moveLista.append('pegar')
        
    position += 1
    
print(f'\n{moveLista}\n')
        
        
    