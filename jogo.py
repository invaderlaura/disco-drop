import pygame
import random

disco_lista = []
disco_velocidade = 0.5
dj = pygame.image.load("assets/djmaicon.gif")
disco = pygame.image.load("assets/cd.gif")
player = pygame.image.load("assets/skittlesgirldoll.gif")


pygame.init()
altura = 1000
largura = 600

pygameDisplay = pygame.display
fundo = pygameDisplay.set_mode(altura, largura)
pygameDisplay.set_caption("Disco Drop")
fundo.fill(0, 0, 0)
pygame.display.flip()

gameEvents = pygame.event
clock = pygame.time.Clock()

gameIcon = pygame.image.load("assets/iconCd.png")
pygameDisplay.set_icon(gameIcon)

fimJogo = False

while fimJogo == False:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fimJogo = True


#gameIcon = pygame.image.load("assets/TrupperIco.ico")
#pygameDisplay.set_icon(gameIcon)