n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

print('\nA soma entre eles é: {}'.format(n1+n2))
print('A subtração entre eles é: {}'.format(n1-n2))
print('A multiplicação entre eles é: {}'.format(n1*n2))
print('A divisão entre eles é: {:.2f}'.format(n1/n2))
#print('A divisão inteira entre eles é: {}, e o resto da divisão é: {}'.format(n1//n2, n1%n2))
print('A divisão inteira entre eles é: {}, '.format(n1//n2),end='')
print('e o resto da divisão é: {}'.format(n1%n2))
#O end não quebra a linha entre dois prints e imprime o conteúdo deles na mesma linha. Entre as aspas podemos deixar vazio ou colocar qualquer conteúdo que será mostrado entre estas duas linhas.
print('{} elevado a {} é: {}'.format(n1,n2,n1**n2))
