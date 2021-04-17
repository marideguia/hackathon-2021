import pygame
import random
import math

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
flagX = random.randint(0, 725)
flagY = random.randint(50, 350)
flagX_change = 0.3
flagY_change = 40

# star
starImg = pygame.image.load('shooting-star.png')
# star coordinates by pixel: x - Left to right, y - Top to bottom
# you need to rotate the image
starX = 0
starY = 480
starX_change = 0
starY_change = .5
star_state = "ready"

score = 0

# FN DEF: Displays player on the screen
def player(x, y):
    # Draws the player on the screen
    screen.blit(playerImg, (x, y))


# FN DEF: Displays flag on the screen
def flag(x, y):
    screen.blit(flagImg, (x, y))


def fire_star(x, y):
    global star_state
    star_state = "fire"
    screen.blit(starImg, (x + 16, y + 10))


def isCollision(flagX, flagY, starX, starY):
    distance = math.sqrt((math.pow(flagX - starX, 2)) + (math.pow(flagY - starY, 2)))
    if distance < 64  :
        return True
    else:
        return False


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

        # Keystroke is an 'event'
        # if keystroke pressed, check if right or left
        # if keystroke released, stop moving
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if star_state is "ready":
                    # get the current x coordinate of the spaceship
                    starX = playerX
                    fire_star(starX, starY)
        # If keystroke released, stop moving
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Display player on screen
    playerX += playerX_change

    # Create boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Display flag on screen
    flagX += flagX_change

    # Flag movement
    if flagX <= 0:
        flagX_change = 0.3
        flagY += flagY_change
    elif flagX >= 730:
        flagX_change = -0.3
        flagY += flagY_change
    # if flag hits lower bound, change y direction and move up
    if flagY >= 350:
        flagY_change = -40
        flagY += flagY_change
    # if flag hits upper bound, change y direction and move down
    if flagY >= 350:
        flagY_change = -40
    elif flagY <= 0:
        flagY_change = 40
        flagY += flagY_change
        flagY_change = 40
        flagY += flagY_change

    #  star movement
    if starY <= 0:
        starY = 480
        star_state = "ready"

    if star_state == "fire":
        fire_star(starX, starY)
        starY -= starY_change

    # collison
    collison = isCollision(flagX, flagY, starX, starY)
    if collison:
        starY = 480
        star_state = "ready"
        score += 1
        print(score)
        flagX = random.randint(0, 800)
        flagY = random.randint(50, 150)

    player(playerX, playerY)
    flag(flagX, flagY)

    # Continuously update display
    pygame.display.update()
