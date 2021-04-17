import pygame
import random
import math
from pygame import mixer

# Initialize the pygame
pygame.init()

# Create the screen: w, h
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('colorful-abstract-universe-textured-background.jpg')

# background sound
mixer.music.load('bicycle.mp3')
mixer.music.play(-1)

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

# Flags
flagImg = []
flagX = []
flagY = []
flagX_change = []
flagY_change = []
num_of_flags = 5

# array
flagImg.append(pygame.image.load('us.png'))
# Flag coordinates by pixel: x - Left to right, y - Top to bottom
flagX.append(random.randint(0, 725))
flagY.append(random.randint(50, 350))
flagX_change.append(0.3)
flagY_change.append(40)

flagImg.append(pygame.image.load('uk.png'))
flagX.append(random.randint(0, 725))
flagY.append(random.randint(50, 350))
flagX_change.append(0.3)
flagY_change.append(40)

flagImg.append(pygame.image.load('china.png'))
flagX.append(random.randint(0, 725))
flagY.append(random.randint(50, 350))
flagX_change.append(0.3)
flagY_change.append(40)

flagImg.append(pygame.image.load('canada.png'))
flagX.append(random.randint(0, 725))
flagY.append(random.randint(50, 350))
flagX_change.append(0.3)
flagY_change.append(40)

flagImg.append(pygame.image.load('japan.png'))
flagX.append(random.randint(0, 725))
flagY.append(random.randint(50, 350))
flagX_change.append(0.3)
flagY_change.append(40)


# Flag
# flagImg = pygame.image.load('us.png')
# flagX = random.randint(0, 725)
# flagY = random.randint(50, 350)
# flagX_change = 0.3
# flagY_change = 40

# star
starImg = pygame.image.load('shooting-star.png')
# star coordinates by pixel: x - Left to right, y - Top to bottom
# you need to rotate the image
starX = 0
starY = 480
starX_change = 0
starY_change = 2
star_state = "ready"

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)


def game_over_text():
    over_text = over_font.render("YOU WIN", True, (255, 255, 255))
    screen.blit(over_text, (235, 250))

def show_score(x,y):
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))

# FN DEF: Displays player on the screen
def player(x, y):
    # Draws the player on the screen
    screen.blit(playerImg, (x, y))


# FN DEF: Displays flag on the screen
def flag(x, y, i):
    screen.blit(flagImg[i], (x, y))


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
                    star_sound = mixer.Sound('laser.wav')
                    star_sound.play()
                    # get the current x coordinate of the star
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


    # Flag movement
    for i in range(num_of_flags):
        if score_value == 5:
            for j in range(num_of_flags):
                flagY[j] = 2000
            game_over_text()
            break

        flagX[i] += flagX_change[i]
        if flagX[i] <= 0:
            flagX_change[i] = 0.3
            flagY[i] += flagY_change[i]
        elif flagX[i] >= 730:
            flagX_change[i] = -0.3
            flagY[i] += flagY_change[i]

    # if flag hits lower bound, change y direction and move up
        if flagY[i] >= 350:
            flagY_change[i] = -40
            flagY[i] += flagY_change[i]
        # if flag hits upper bound, change y direction and move down
        if flagY[i] >= 350:
            flagY_change[i] = -40
        elif flagY[i] <= 0:
            flagY_change[i] = 40
            flagY[i] += flagY_change[i]
            flagY_change[i] = 40
            flagY[i] += flagY_change[i]

        # collison
        collison = isCollision(flagX[i], flagY[i], starX, starY)
        if collison:
            hit_sound = mixer.Sound('explosion.wav')
            hit_sound.play()
            starY = 480
            star_state = "ready"
            score_value += 1
            flagX[i] = random.randint(0, 800)
            flagY[i] = random.randint(50, 150)

        flag(flagX[i], flagY[i], i)

    #  star movement
    if starY <= 0:
        starY = 480
        star_state = "ready"

    if star_state == "fire":
        fire_star(starX, starY)
        starY -= starY_change



    player(playerX, playerY)
    show_score(textX, textY)
    # Continuously update display
    pygame.display.update()
