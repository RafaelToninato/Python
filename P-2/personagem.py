import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480

preto = 0, 0, 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sprites')


class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/homem_terno_0.png'))
        self.sprites.append(pygame.image.load('sprites/homem_terno_1.png'))
        self.sprites.append(pygame.image.load('sprites/homem_terno_2.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (32 * 5, 32 * 5))

        self.rect = self.image.get_rect()
        self.rect.topleft = 200, 300

    def update(self):
        self.atual = self.atual + 0.1
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (32 * 5, 32 * 5))


tsprites = pygame.sprite.Group()
personagem = Personagem()
tsprites.add(personagem)

imagem_fundo = pygame.image.load('sprites/cidade_fundo.jpg').convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))

relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill(preto)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    tela.blit(imagem_fundo, (0, 0))
    tsprites.draw(tela)
    tsprites.update()
    pygame.display.flip()