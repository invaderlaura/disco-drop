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
fonte = pygame.font.Font('freesansbold.ttf', 16)

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

# deixa cores da moldura alternando
fundo = (10, 10, 10)
rosa = (255, 102, 102)
azul = (0, 0, 255)
azulClaro = (135, 206, 235)
branco = (255, 255, 255)


def desenhaMoldura(cor):
    pygame.draw.rect(tela, cor, pygame.Rect(0, 0, 510, 145))
    tela.blit(dj, (10, 20))
    pygame.draw.rect(tela, cor, pygame.Rect(0, 145, 10, 535))
    pygame.draw.rect(tela, cor, pygame.Rect(500, 145, 510, 535))
    pygame.draw.rect(tela, cor, pygame.Rect(0, 660, 510, 670))
    pygame.display.flip()


# variaveis do disco
posicIncialDisco = 115
posicFinalDisco = 660
discoX = random.randrange(0, largura)
discoY = posicIncialDisco
velocidade = 0.5
discosPerdidos = 0
discosColetados = 0
discoLista = []

# variaveis do player
playerX = 204
playerY = 564
movimentoXPlayer = 0
colisao = False

# exibe mensagem de fim de jogo


def fimJogo():
    for event in gameEvents.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    texto1 = fonte.render(
        "Você perdeu o ritmo e deixou três discos caírem.", True, branco)
    texto2 = fonte.render(
        "A festa acabou!", True, branco)
    texto3 = fonte.render(
        f'Discos coletados: {discosColetados}', True, branco)
    mostraJogo()
    tela.blit(texto2, (190, 300))
    tela.blit(texto1, (60, 320))
    tela.blit(texto3, (170, 340))
    pygame.mixer.music.stop()


# atualiza tela
def mostraJogo():
    desenhaMoldura(rosa)
    tela.fill(fundo)
    tela.blit(player, (playerX, playerY))
    tela.blit(disco, (discoX, discoY))
    tela.blit(truss, (29.5, 155))
    numDiscosPerdidos = fonte.render(
        f'Discos perdidos: {discosPerdidos}', True, rosa)
    tela.blit(numDiscosPerdidos, (25, 210))
    numDiscosColetados = fonte.render(
        f'Discos coletados: {discosColetados}', True, azulClaro)
    tela.blit(numDiscosColetados, (325, 210))
    desenhaMoldura(azul)


running = True
perdeu = False

while running:
    for event in gameEvents.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movimentoXPlayer = -0.5
            elif event.key == pygame.K_RIGHT:
                movimentoXPlayer = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                movimentoXPlayer = 0

    playerX = playerX + movimentoXPlayer
    discoY = discoY + velocidade

    # só atualiza a tela enquanto o player não perder
    if perdeu == False:
        mostraJogo()

    # limita movimento do player dentro das bordas
    if playerX <= 10 or playerX >= 449:
        movimentoXPlayer = 0

    # volta o primeiro disco pro começo
    if discoY >= posicFinalDisco:
        discoY = posicIncialDisco
        discoX = random.randrange(0, largura)
        discosPerdidos += 1

    if colisao:
        discosColetados += 1

    # termina o jogo
    if discosPerdidos == 3:
        discoY = posicFinalDisco
        perdeu = True
        fimJogo()

    pygame.display.flip()
