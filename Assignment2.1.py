#Importing pygame.
import pygame
pygame.init()

#Sets the display window size for the game.
win = pygame.display.set_mode((1000, 1000))

#Sets the top left hand side of the screen to display what he file is called.
pygame.display.set_caption("Assignment 2")

screenWidth = 1000
#Player start position, size and movement capabilities.
x = 50
y = 50
width = 40
height = 60
vel = 7

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

#Fills in the display with black to stop the rectangle drawing my than one.
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()



