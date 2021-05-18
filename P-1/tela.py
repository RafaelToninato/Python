import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.load('bgm_1.mp3')
pygame.mixer.music.play(-1)

sfx = pygame.mixer.Sound('sfx_1.wav')
sfx.set_volume(0.5)

largura = 640
altura = 480
x_cobra = int(largura / 2)
y_cobra = int(altura / 2)

x_cntl = 40
y_cntl = 0

x_maca = randint(40, 600)
y_maca = randint(40, 440)

fonte = pygame.font.SysFont('arial', 30, True, False)
pontos = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('P-1')
relogio = pygame.time.Clock()
lcobra = []
cinicial = 3
morreu = False


def acobra(l_cobra):
    for XeY in l_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 40, 40))


def rjogo():
    global pontos, cinicial, x_maca, x_cobra, y_cobra, y_maca, lcobra, lcabeca, morreu
    pontos = 0
    cinicial = 3
    x_cobra = int(largura / 2)
    y_cobra = int(altura / 2)
    lcobra = []
    lcabeca = []
    x_maca = randint(40, 600)
    y_maca = randint(40, 440)
    morreu = False


while True:
    relogio.tick(10)
    tela.fill((200, 200, 200))
    msm = f'Pontos: {pontos}'
    txt_format = fonte.render(msm, False, (255, 255, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_cntl == 40:
                    pass
                else:
                    x_cntl = -40
                    y_cntl = 0
            if event.key == K_d:
                if x_cntl == -40:
                    pass
                else:
                    x_cntl = 40
                    y_cntl = 0
            if event.key == K_w:
                if y_cntl == 40:
                    pass
                else:
                    x_cntl = 0
                    y_cntl = -40
            if event.key == K_s:
                if y_cntl == -40:
                    pass
                else:
                    x_cntl = 0
                    y_cntl = 40

    x_cobra = x_cobra + x_cntl
    y_cobra = y_cobra + y_cntl
    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 40, 40))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 40, 40))

    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos = pontos + 1
        sfx.play()
        cinicial = cinicial + 1

    lcabeca = [x_cobra, y_cobra]
    lcobra.append(lcabeca)

    if lcobra.count(lcabeca) > 1:
        f2 = pygame.font.SysFont('arial', 20, True, False)
        msm = 'Game over! Pressione a tecla R para jogar novamente'
        txt_format = f2.render(msm, True, (255, 255, 0))
        ret_texto = txt_format.get_rect()

        morreu = True
        while morreu:
            tela.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        rjogo()

            ret_texto.center = (largura // 2, altura // 2)
            tela.blit(txt_format, ret_texto)
            pygame.display.update()

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0

    if len(lcobra) > cinicial:
        del lcobra[0]

    acobra(lcobra)

    tela.blit(txt_format, (450, 40))
    pygame.display.update()
