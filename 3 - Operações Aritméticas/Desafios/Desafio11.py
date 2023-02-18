#Faça um programa que leia a largura e a altura de uma parede, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2,0 metros quadrados.

h = float(input('Digite a altura da parede: '))
l = float(input('Digite a largura da parede: '))
r = float(input('Cada litro de tinta pinta quantos m²? '))
print('A área da parede é de: {:.2f} m²'.format(h*l)) #Aperte o alt direito e o número que você deseja ser expoente.
print('Serão necessários {} litros de tinta para pintá-la.'.format((h*l) / r))
