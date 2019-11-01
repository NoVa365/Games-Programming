#Importing pygame functionality.
import pygame
import random
import time
pygame.init()

#Sets the window size for the game.
win = pygame.display.set_mode((800, 600))

#This sets the name of the program in the top left abpve the display.
pygame.display.set_caption("Assignment 2 Reassignment")

screenWidth = 1000
RED = (255, 0, 0)
#rockSpeed = 5
#rock_y = 0
#rock_x = 0
#Coordinates for where the player will appear.
x = 400
y = 725
#Creates the size of the rectangle (Will be changed for a sprite at a later date).
width = 40
height = 60
#Measures the speed in which the player is able to move.
vel = 5

#Sprite variables to load into the game.
playerImage = pygame.image.load("frogsprite.png").convert_alpha()
playerImage.set_colorkey((255, 255, 255))
pl = pygame.transform.scale(playerImage, (100, 100))


rockSprite = pygame.image.load("rock.png").convert_alpha()
rockSprite.set_colorkey((255, 255, 255))
rockImage = pygame.transform.scale(rockSprite, (100, 100))

butterflyImage = pygame.image.load("butterfly.png").convert_alpha()
butterflyImage.set_colorkey((255, 255, 255))
bf = pygame.transform.scale(butterflyImage, (100, 100))

background = pygame.image.load("background.jpg").convert_alpha()
#background_size = pygame.transfrom.scale(background, (800, 600))
background_size = pygame.transform.scale(background, (800, 600))
last_butterfly_spawn = 0
last_rock_spawn = 0
butterflyTimer = 0


#background = pygame.image.load("background.jpg").convert_alpha()

#Player class to create the player object


class Player:
    def __init__(self):
        self.x = 400
        self.y = 500

    def draw(self):
        win.blit(pl, (self.x, self.y))

    def move(self):
        if pressed_keys[pygame.K_a] and self.x > 0:
            self.x -= 5

        if pressed_keys[pygame.K_d] and self.x < 800 - width - vel:
            self.x += 5
	
    def eat(self):
        if player_click[0]:
            pygame.draw.line(win, (255, 0, 0), (self.x + 80, self.y + 38), cursor, 5)



        #pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))


player = Player()

#Creates the rocks that will be falling from the sky.


class Rock:
    def __init__(self):
        self.x = random.randint(0, 600)
        self.y = -2
        self.speed = random.randint(1, 3)

    def draw(self):
        win.blit(rockImage, (self.x, self.y))
        # pygame.draw.circle(win, (255,0,0), (self.x, self.y), 2)

    def move(self):
        self.y += self.speed


rocklist = []


class Butterflies:
    def __init__(self):
        self.x = random.randint(0, 600)
        self.y = random.randint(0, 400)

    def move(self):
        self.y += 2
        self.x = self.dx

    def draw(self):
        win.blit(bf, (self.x, self.y))

    def hit_by(self):
        pass




butterflylist = []





#Main gameplay loop (Mainly used for testing)
run = True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    if time.time() - last_butterfly_spawn > 0.9:
        butterflylist.append(Butterflies())
        last_butterfly_spawn = time.time()


    if time.time() - last_rock_spawn > 0.3:
        rocklist.append(Rock())
        last_rock_spawn = time.time()







    pressed_keys = pygame.key.get_pressed()
    player_click = pygame.mouse.get_pressed()
    cursor = pygame.mouse.get_pos()
#This is to make the player be able to move using the arrow keys.
    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_a] and x > 0:
        #x -= vel

    #if keys[pygame.K_d] and x < 800 - width - vel:
            #x += vel

    #player_click = pygame.mouse.get_pressed()[1]


# RENDERING PART
#Fills in the display with black to stop the rectangle drawing more than one.

    win.fill((0, 0, 0))
    win.blit(background_size, [0, 0])
    player.draw()
    player.move()
    player.eat()
    butterflyTimer += 1


    e = 0
    while e < len(rocklist):
        rocklist[e].move()
        rocklist[e].draw()
        if rocklist[e].y > 800:
            del rocklist[e]
            e -= 1

        e += 1

    b = 0
    while b < len(butterflylist):
        butterflylist[b].draw()
        if butterflylist[b] or time.time(butterflyTimer) >= 5:
            del butterflylist[b]
            b -= 1

        b += 1






    pygame.display.update()


pygame.quit()





