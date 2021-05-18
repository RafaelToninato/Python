import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange

pygame.init()
pygame.mixer.init()

dirp = os.path.dirname(__file__)
diri = os.path.join(dirp, 'imagens')
dirs = os.path.join(dirp, 'sons')

largura = 640
altura = 480

branco = 255, 255, 255

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Dino Game')

sprite_sheet = pygame.image.load(os.path.join(diri, 'dinoSpritesheet.png')) \
    .convert_alpha()

som_colisao = pygame.mixer.Sound(os.path.join(dirs, 'death_sound.wav'))
som_colisao.set_volume(1)
colidiu = False


class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.som_pulo = pygame.mixer.Sound(os.path.join(dirs, 'jump_sound.wav'))
        self.som_pulo.set_volume(1)
        self.imag_dino = []
        for i in range(3):
            img = sprite_sheet.subsurface((i * 32, 0), (32, 32))
            img = pygame.transform.scale(img, (32 * 3, 32 * 3))
            self.imag_dino.append(img)

        self.indl = 0
        self.image = self.imag_dino[self.indl]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.pos_y_inicial = 416 - 96 // 2
        self.rect.center = (100, 416)
        self.pulo = False

    def pular(self):
        self.pulo = True
        self.som_pulo.play()

    def update(self):
        if self.pulo:
            if self.rect.y <= 240:
                self.pulo = False
            self.rect.y -= 20
        else:
            if self.rect.y < self.pos_y_inicial:
                self.rect.y += 20
            else:
                self.rect.y = self.pos_y_inicial

        if self.indl > 2:
            self.indl = 0
        self.indl += 0.25
        self.image = self.imag_dino[int(self.indl)]


class Nuvens(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7 * 32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32 * 3, 32 * 3))
        self.rect = self.image.get_rect()

    def update(self):
        if self.rect.x < -64:
            self.rect.x = largura
            self.rect.y = randrange(00, 100, 50)
            self.rect.x = randrange(650, 1000, 50)
        self.rect.x -= 8


class Chao(pygame.sprite.Sprite):
    def __init__(self, pos_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((6 * 32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32 * 2, 32 * 2))
        self.rect = self.image.get_rect()
        self.rect.y = altura - 64
        self.rect.x = pos_x * 64

    def update(self):
        if self.rect.x < -64:
            self.rect.x = largura
            self.rect.x = randrange(640, 704, 64)
        self.rect.x -= 8


class Cacto(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32 * 2, 32 * 2))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (largura, altura - 64)

    def update(self):
        if self.rect.x < -64:
            self.rect.x = largura
            self.rect.x = randrange(640, 704, 64)
        self.rect.x -= 8


tsprites = pygame.sprite.Group()
dino = Dino()
tsprites.add(dino)

for i in range(3):
    nuvem = Nuvens()
    tsprites.add(nuvem)

for i in range(640 * 2 // 64):
    chao = Chao(i)
    tsprites.add(chao)

cacto = Cacto()
tsprites.add(cacto)

gobstaculos = pygame.sprite.Group()
gobstaculos.add(cacto)

relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill(branco)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if dino.rect.y != dino.pos_y_inicial:
                    pass
                else:
                    dino.pular()

    colisoes = pygame.sprite.spritecollide(dino, gobstaculos, False, pygame.sprite.collide_mask)

    tsprites.draw(tela)

    if colisoes and colidiu == False:
        som_colisao.play()
        colidiu = True
    if colidiu:
        pass
    else:
        tsprites.update()

    pygame.display.flip()
