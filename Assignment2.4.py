#Importing pygame functionality.
import pygame
import random
pygame.init()

#Sets the window size for the game.
win = pygame.display.set_mode((800,800))

#This sets the name of the program in the top left abpve the display.
pygame.display.set_caption("Assignment 2 Reassignment")

screenWidth = 1000
RED = (255,0,0)
#rockSpeed = 5
#rock_y = 0
#rock_x = 0
#Coordinates for where the player will appear.
x = 400
y = 725
#Creats the size of the rectangle (Will be changed for a sprite at a later date).
width = 40
height = 60
#Measures the speed in which the player is able to move.
vel = 5
#player = pygame.image.load("frogSprite").convert_alpha()
rockSprite = pygame.image.load("rock").convert_alpha()

class Player:
    def __init__(self):
        self.x = 400
        self.y = 725
    def draw(self):
        #win.blit(player, (self.x, self.y))
        pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))

player = Player()

class Rock:
    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = -2
        self.speed = random.randint(5,7)
    def draw(self):
        win.blit(rockSprite), (self.x, self.y)
        #win(255,0,0 (self.x, self.y), 2)
    def move(self):
        self.y += self.speed

rocklist = []

#Main gameplay loop (Mainly used for testing)
run = True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

#This is to make the player be able to move using the arrow keys.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and x > 0:
        x -= vel

    if keys[pygame.K_d] and x < 800 - width - vel:
            x += vel

    #rock_y = rock_y + rockSpeed
    #if rockSpeed > height:
       # rock_x = random.randrange(0,width)
       # rock_y = -25

    for r in rocklist:
        r.move()
        r.draw()



    #Fills in the display with black to stop the rectangle drawing my than one.
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))
    pygame.display.update()
    rocklist.append(Rock())


pygame.quit()




