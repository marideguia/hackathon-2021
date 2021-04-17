import pygame
import random

# Initialize the pygame
pygame.init()

# Create the screen: w, h
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('colorful-abstract-universe-textured-background.jpg')

# Title and Icon (32 pixels)
icon = pygame.image.load('us.png')  # ***Change game icon***
pygame.display.set_icon(icon)
pygame.display.set_caption("Earth Discovery")

# Player
playerImg = pygame.image.load('student.png')
# Player coordinates by pixel: x - Left to right, y - Top to bottom
playerX = 355
playerY = 500
playerX_change = 0

# Flag
flagImg = pygame.image.load('us.png')
# Flag coordinates by pixel: x - Left to right, y - Top to bottom
flagX = random.randint(0, 800)
flagY = random.randint(50, 350)
flagX_change = 0.3
flagY_change = 40


# FN DEF: Displays player on the screen
def player(x, y):
    screen.blit(playerImg, (x, y))


# FN DEF: Displays flag on the screen
def flag(x, y):
    screen.blit(flagImg, (x, y))


# Game Loop
running = True
while running:
    # Background Color: R, G, B
    screen.fill((128, 128, 255))
    # Background image
    screen.blit(background, (-800, -1500))

    # Exit game when player QUITS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keystroke events - Player movement
        # If keystroke pressed, check if right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        # If keystroke released, stop moving        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    #Apply player movement
    playerX += playerX_change

    # Create player movement boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Apply flag movement
    flagX += flagX_change

    # Flag movement 
    # if flag hits left bound, change x direction and move up/down
    if flagX <= 0:
        flagX_change = 0.3
        flagY += flagY_change
    # if flag hits right bound, change x direction and move up/down
    elif flagX >= 730:
        flagX_change = -0.3
        flagY += flagY_change
    # if flag hits lower bound, change y direction and move up
    if flagY >= 350:
        flagY_change = -40
        flagY += flagY_change
    # if flag hits upper bound, change y direction and move down
    elif flagY <= 0:
        flagY_change = 40
        flagY += flagY_change

    # Update player position
    player(playerX, playerY)
    # Update flag position
    flag(flagX, flagY)

    # Continuously update display
    pygame.display.update()
