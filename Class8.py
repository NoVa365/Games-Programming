import pygame, sys
from pygame.locals import *
pygame.init()
pygame.display.set_caption("My first PyGame program")
screen = pygame.display.set_mode((640,480))
import random

xpos = random.randint (0,640)
ypos = random.randint(0,480)
#clock = pygame.time.Clock()

class Raindrop:

    def __init__(self):
        self.x = random.randint (0,640)
        self.y = 0

    def move(self):
        self.y += 1

    def draw(self):
        pygame.draw.circle(screen,(131,139,139),(self.x,self.y),5,2)



while 1:
    #clock.tick(80)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
                 #R  G B
    screen.fill((120,90,90))
    #pressed_key = pygame.key.get_pressed()
    pygame.draw.circle(screen,(131,139,139),(xpos,ypos),5,2)

    #if pressed_key[K_RIGHT] and xpos <= 640:
        #xpos+=1
    #if pressed_key[K_LEFT] and xpos >= 0:
        #xpos-=1
    #if pressed_key[K_UP] and ypos >= 0:
        #ypos-=1
    #if pressed_key[K_DOWN] and ypos <= 480:
    ypos+=1

    pygame.display.update()
