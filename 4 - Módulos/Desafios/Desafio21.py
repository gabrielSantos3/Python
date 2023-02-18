#Faça um programa que abra e reproduza um arquivo mp3.
import pygame
import emoji

print('\nMelhores cantadas do quadro "Vai dar namoro" \n')
print(emoji.emojize(':sparkling_heart:')*15)
print('\nCantada 1: Gata, você teria um dicionário para me emprestar? É porque quando vi sua beleza, eu fiquei completamente sem palavras.')
print('Cantada 2: Gata, você teria um mapa para me emprestar? É porque eu me perdi no brilho dos seus olhos.')
print('Cantada 3: Seu nome é Mentira? É porque você é bonita demais para ser verdade.')
print('Cantada 4: No mar navega o barco, no barco navega o vento; nas ondas dos seus cabelos, navega o meu pensamento.')
print('Cantada 5: Você tem uma caneta? É que eu quero começar a escrever a nossa história.')
print('Cantada 6: O que eu sinto por você só pode ser motorista, porque passageiro não é.')
print('Cantada 7: Você Você não fica com dor no corpo por carregar toda a beleza do mundo nas costas?')
print('Cantada 8: Eu comprei um shampoo anti-quedas, mas vou devolver porque não funciona. Mesmo usando ele, ainda continuo caidinho por você.')
print('Cantada 9: Você ainda tem dois pedidos pra fazer ao Gênio da Lâmpada. O primeiro foi para encontrar o amor da sua vida, e olha eu aqui!')
print('Cantada 10: Gata, você é uma fogueira? É porque quando te vejo, meu coração arde em chamas.')

# Iniciando o Pygame
pygame.init()
#Selecionando a música
pygame.mixer.music.load('Careless.mp3')
#Dando play na música
pygame.mixer.music.play(loops=0, start=0.0)
#O Pygame sofreu lagumas alterações, agora é necessário inserir um input.
input()
#Espera o evento terminar para encerrar o programa
pygame.event.wait()
