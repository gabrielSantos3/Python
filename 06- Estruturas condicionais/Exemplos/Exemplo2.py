n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
n3 = float(input('Digite a sua terceira nota: '))

media = (n1 + n2 + n3) / 3

print(f'A sua média foi: {media:.2f}')
print('Parabéns!' if media >= 6 else 'Estude mais!')