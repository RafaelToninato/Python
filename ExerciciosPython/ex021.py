import pygame
print('O programa está tocando agora Gangsta Paradise')
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('Paradise.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
