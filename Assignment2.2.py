#Importing pygame.
import pygame
import random
WIDTH = 1920
HEIGHT = 1080
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))



clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()


#Sets the display window size for the game.
win = pygame.display.set_mode((WIDTH, HEIGHT))

#Sets the top left hand side of the screen to display what he file is called.
pygame.display.set_caption("Assignment 2")


bg = pygame.image.load('Background.jpg')


screenWidth = 1920
#Player start position, size and movement capabilities.
x = 50
y = 50
width = 40
height = 60
vel = 15


#class Player(pygame.sprite.Sprite):
    #def __init__(self):
        #pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((50, 40))
        #self.image.fill(GREEN)
        #self.rect = self.image.get_rect()
        #self.rect.centerx = WIDTH / 2
        #self.rect.bottom = HEIGHT - 10
        #self.speedx = 0

    #def update(self):
        #self.rect.x += self.speedx


#Fills in the display with black to stop the rectangle drawing my than one.
def redrawGameWindow():
    win.blit(bg, (0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()


#class Mob(pygame.sprite.Sprite):
    #def __init__(self):
        #pygame.sprite.Sprite.__init(self)
        #self.image = pygame.Surface((30, 40))
        #self.image.fill(RED)
        #self.rect = self.image.get_rect()
        #self.rect.x = random.randrange(0, width - self.rect.width)
        #self.rect.y = random.randrange(-100, -40)
        #self.speedy = random.randrange(1, 8)


#def update(self):
    #self.rect.y += self.speedy
    #if self.rect.top > HEIGHT + 10:
        #self.rect.x = random.randrange(0, width - self.rect.width)
        #self.rect.y = random.randrange(-100, -40)
        #self.speedy = random.randrange(1, 8)

#all_sprites = pygame.sprite.Group()
#mobs = pygame.sprite.Group()
#player = Player()
#all_sprites.add(player)
#for i in range(8):
    #m = Mob()
    #all_sprites.add(m)
    #mobs.add(m)

#Gameplay loop for movement.
run = True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

#Movement for the player when key is pressed + the speed at which they can move. Also stops the player from going outside boarder.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and x > vel:
        x -= vel

    if keys[pygame.K_d] and x < screenWidth - width - vel:
        x += vel

    if keys[pygame.K_w] and y > vel:
        y -= vel

    if keys[pygame.K_s] and y < screenWidth - height - vel:
        y += vel

    redrawGameWindow()
    all_sprites.update()
    all_sprites.draw(screen)


#class Projectile(object):
    #def__init__(self,x y, radius, colour, facing):
        #self.x = x
        #self.y = y
        #self. radius = radius
        #self.colour = colour
        #self.facing = facing
        #self.vel = 8 * facing

    #def draw(win):
        #pygame.draw.circle(win, self.colour, (self.x, self.y), self.radius)


pygame.quit()



