nome = input('Digite seu nome: ')
size = len(nome)

if(size > 10):
    print('Seu nome é tão grande!')
elif(size > 4):
    print('Tamanho do nome aceitável')
else:
    print('Seu nome é tão pequeno!')