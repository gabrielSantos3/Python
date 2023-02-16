#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

met = float(input('Digite a quantidade de metros que você deseje converter: '))

print('{} m'.format(met),end=' >>>> ')
print('{:.0f} cm'.format(met*100), end=" >>>> ")
print('{:.0f} mm'.format(met*1000))
