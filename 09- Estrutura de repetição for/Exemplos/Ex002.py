nome = 'Gabriel'

for i in range(0, len(nome)):
    print(nome[i])
    
print('\n\n')


'''
-> Percorre a string de trás pra frente. O último parâmetro é a iteração, ou seja, o que vai acontecer no final do laço. Subtrai 1. 

-> Começa na posição final (tamanho da string -1), vai até a posição 0, decrescendo 1
'''
for i in range(len(nome) - 1, -1, -1):
    print(nome[i])