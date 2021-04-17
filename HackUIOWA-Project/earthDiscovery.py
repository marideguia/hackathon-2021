import pygame
import random

# Initialize the pygame
pygame.init()

# Create the screen: w, h
screen = pygame.display.set_mode((800,600))

# Title and Icon (32 pixels)
icon = pygame.image.load('us.png') # ***Change game icon***
pygame.display.set_icon(icon)
pygame.display.set_caption("Earth Invaders")

# Player
playerImg = pygame.image.load('student.png')
# Player coordinates by pixel: x - Left to right, y - Top to bottom
playerX = 355
playerY = 500
playerX_change = 0

# FN DEF: Displays player on the screen
def player(x,y):
    # Draws the player on the screen
    screen.blit(playerImg, (x, y))

# Game Loop
running = True
while running:
    # Background Color: R, G, B
    screen.fill((128, 128, 255))

    # Exit game when player QUITS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keystroke is an 'event'
        # if keystroke pressed, check if right or left
        # if keystroke released, stop moving
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    # Display player on screen
    playerX += playerX_change
    player(playerX,playerY)

    # Continously update display
    pygame.display.update()


