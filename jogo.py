import pygame
import random

pygame.init()
pygame.mixer.init()

altura = 670
largura = 510
tamanho = (largura, altura)

pygameDisplay = pygame.display
gameIcon = pygame.image.load("assets/iconCd.png")
pygameDisplay.set_icon(gameIcon)
tela = pygameDisplay.set_mode(tamanho)
pygameDisplay.set_caption("Disco Drop")
gameEvents = pygame.event
clock = pygame.time.Clock()

dj = pygame.image.load("assets/djmaicon.gif")
disco = pygame.image.load("assets/cd.gif")
player = pygame.image.load("assets/SkittlesGirlDOLL.gif")
truss = pygame.image.load("assets/truss.gif")

# define playlist
playlist = list()
playlist.append("assets/musicas/cant_get_over.mp3")
playlist.append("assets/musicas/lamour_toujours.mp3")
playlist.append("assets/musicas/stereo_love.mp3")
playlist.append("assets/musicas/better_off_alone.mp3")
playlist.append("assets/musicas/infinity_2008.mp3")

# escolhe musica
pygame.mixer.music.load(random.choice(playlist))
pygame.mixer.music.queue(random.choice(playlist))
pygame.mixer.music.play()
pygame.mixer.music.set_endevent(pygame.USEREVENT)

fundo = (10, 10, 10)
rosa = (255, 102, 102)
azul = (0, 0, 255)


def desenhaMoldura(cor):
    pygame.draw.rect(tela, cor, pygame.Rect(0, 0, 510, 145))
    tela.blit(dj, (10, 20))
    pygame.draw.rect(tela, cor, pygame.Rect(0, 145, 10, 535))
    pygame.draw.rect(tela, cor, pygame.Rect(500, 145, 510, 535))
    pygame.draw.rect(tela, cor, pygame.Rect(0, 660, 510, 670))
    pygame.display.flip()


discosPerdidos = []
discoVelocidade = 0.5
discoX = random.randrange(0, largura)
discoY = 0
playerX = 204
playerY = 564
movimentoXPlayer = 0

running = True

while running:
    for event in gameEvents.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movimentoXPlayer = -0.3
            elif event.key == pygame.K_RIGHT:
                movimentoXPlayer = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                movimentoXPlayer = 0

    playerX = playerX + movimentoXPlayer
    desenhaMoldura(rosa)
    tela.fill(fundo)
    tela.blit(truss, (29.5, 155))
    tela.blit(player, (playerX, playerY))
    desenhaMoldura(azul)
    pygame.display.flip()
