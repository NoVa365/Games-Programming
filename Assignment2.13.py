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
#playerImage = pygame.image.load("frogsprite.png").convert_alpha()
#playerImage.set_colorkey((255, 255, 255))
#pl = pygame.transform.scale(playerImage, (100, 100))



#rockSprite = pygame.image.load("rock.png").convert_alpha()
#rockSprite.set_colorkey((255, 255, 255))
#rockImage = pygame.transform.scale(rockSprite, (100, 100))

butterflyImage = pygame.image.load("butterfly.png").convert_alpha()
butterflyImage.set_colorkey((255, 255, 255))
bf = pygame.transform.scale(butterflyImage, (100, 100))

background = pygame.image.load("background.jpg").convert_alpha()
#background_size = pygame.transfrom.scale(background, (800, 600))
background_size = pygame.transform.scale(background, (800, 600))
last_butterfly_spawn = 0
last_rock_spawn = 0
butterflyTimer = 0
tongue_sound = pygame.mixer.Sound("Yoshi.wav")
music = pygame.mixer.music.load("Music.mp3")
pygame.mixer.music.play(+3)




#Player class to create the player object

class Player(pygame.sprite.Sprite):

    def __init__(self):

        self.x = 400
        self.y = 500
        self.image = pygame.image.load("frogsprite.png").convert_alpha()
        self.pl = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.pl.get_rect()
        #self.pl.fill(RED)

    def update(self):
        self.rect == self.x, self.y

    def draw(self):
        win.blit(self.pl, (self.x, self.y))
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        #self.hitbox = (self.x + 20, self.y, 60, 80)

    def move(self):
        if pressed_keys[pygame.K_a] and self.x > 0:
            self.x -= 5

        if pressed_keys[pygame.K_d] and self.x < 800 - width - vel:
            self.x += 5

    def eat(self):
        if player_click[0]:
            pygame.draw.line(win, (255, 0, 0), (self.x + 80, self.y + 38), cursor, 5)
            tongue_sound.play()

    def collide(self, rocklist):
        if pygame.sprite.spritecollide(self, rocklist, False):
            print("Hit")
            pygame.quit()


player = Player()

#Creates the rocks that will be falling from the sky.


class Rock(pygame.sprite.Sprite):
    def __init__(self):
        self.x = random.randint(0, 600)
        self.y = -2
        self.speed = random.randint(1, 3)
        self.image = pygame.image.load("rock.png").convert_alpha()
        self.rockImage = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.rockImage.get_rect()
        #self.rockImage.fill(RED)

    def draw(self):
        win.blit(self.rockImage, (self.x, self.y))
        self.rect = self.rockImage.get_rect()

    def move(self):
        self.y += self.speed
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    #def collide(self, spriteGroup):
        #if pygame.sprite.spritecollide(self, spriteGroup, False):
            #remove()


global rocklist
rocklist = []


class Butterflies:
    def __init__(self):
        self.x = random.randint(0, 500)
        self.y = random.randint(100, 200)
        self.speed = random.randint(-1, 3)


    def move(self):
        self.y += self.speed - 2
        self.x += self.speed

    def draw(self):
        win.blit(bf, (self.x, self.y))

    def update(self):
        if time.time() - self.timer >= self.lifetime:
            del self

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


# RENDERING PART
#Fills in the display with black to stop the rectangle drawing more than one.

    win.fill((0, 0, 0))
    win.blit(background_size, [0, 0])
    player.draw()
    player.move()
    player.eat()
    player.update()
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
        butterflylist[b].move()
        if butterflylist[b].x > 800:
            del butterflylist[b]

            b -= 1

        b += 1


    pygame.display.update()

    hit = pygame.sprite.spritecollide(player, rocklist, False)
    if hit:
        print("got hit")
        # run = False

pygame.quit()





