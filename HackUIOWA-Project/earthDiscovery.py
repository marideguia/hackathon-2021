import pygame
import random
import math
from pygame import mixer

# Initialize the pygame
pygame.init()

# Create the screen: w, h
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')

# background sound
mixer.music.load('bicycle.mp3')
mixer.music.play(-1)

# Title and Icon (32 pixels)
icon = pygame.image.load('student.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Earth Discovery")

# Player
playerImg = pygame.image.load('student.png')
# Player coordinates by pixel: x - Left to right, y - Top to bottom
playerX = 355
playerY = 500
playerX_change = 0

# Flags and flag movement rate
flagImg = []
flagX = []
flagY = []
flagX_change = []
flagY_change = []
num_of_flags = 5

# Array for question prompt
country_list = ["USA", "UK", "China", "Canada", "Japan", " "]

# Track country for correct answer
global_i = 0

# Populate arrays with flag attributes
for i in range(num_of_flags):
    flagX.append(random.randint(0, 710))
    flagY.append(random.randint(50, 350))
    flagX_change.append(0.3)
    flagY_change.append(0.3)
flagImg.append(pygame.image.load('us.png'))
flagImg.append(pygame.image.load('uk.png'))
flagImg.append(pygame.image.load('china.png'))
flagImg.append(pygame.image.load('canada.png'))
flagImg.append(pygame.image.load('japan.png'))


# Star attributes
starImg = pygame.image.load('shooting-star.png')
starX = 0
starY = 480
starX_change = 0
starY_change = 2
star_state = "ready"

# Score Attributes
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

# Displays win message
def game_over_text():
    over_text = over_font.render("YOU WIN", True, (255, 255, 255))
    screen.blit(over_text, (235, 250))

# Displays score
def show_score(x,y):
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))

# Displays question
def show_question(x,y):
    question = font.render("Choose the flag for " + country_list[global_i], True, (255, 255, 255))
    screen.blit(question, (x, y))

# Displays player on the screen
def player(x, y):
    screen.blit(playerImg, (x, y))

# Displays flag on the screen
def flag(x, y, i):
    screen.blit(flagImg[i], (x, y))

# Displays star
def fire_star(x, y):
    global star_state
    star_state = "fire"
    screen.blit(starImg, (x + 16, y + 10))

# Checks star collision
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
    # screen.fill((0, 0, 0))
    # Background image
    screen.blit(background, (0, 0))

    # Exit game when player QUITS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check keystroke press and release
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1

            # Check for star launch
            if event.key == pygame.K_SPACE:
                if star_state == "ready":
                    star_sound = mixer.Sound('laser.wav')
                    star_sound.play()
                    # Get the current x coordinate of the star
                    starX = playerX
                    fire_star(starX, starY)

        # If keystroke released, stop moving
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Display player on screen
    playerX += playerX_change

    # Create player boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Flag movement
    for i in range(num_of_flags):
        # Win Condition: move flags off screen and display win message
        if score_value == 5:
            for j in range(num_of_flags):
                flagY[j] = 2000
            game_over_text()
            break

        flagX[i] += flagX_change[i]
        flagY[i] += flagY_change[i]
        # if flag hits left bound, change x direction and move up/down
        if flagX[i] <= 0:
            flagX_change[i] = 0.3
            # flagY[i] += flagY_change[i]
        #if flag hits right bound, change x direction and move up/down
        elif flagX[i] >= 750:
            flagX_change[i] = -0.3
            #flagY[i] += flagY_change[i]

        # if flag hits lower bound, change y direction and move up
        if flagY[i] >= 350:
            flagY_change[i] = -0.3
            #flagY[i] += flagY_change[i]
        # if flag hits upper bound, change y direction and move down
        elif flagY[i] <= 0:
            flagY_change[i] = 0.3
            #flagY[i] += flagY_change[i]

        # Check for collision
        collision = isCollision(flagX[i], flagY[i], starX, starY)
        if collision:
            # If correct flag is hit
            if i == global_i:
                correct_sound = mixer.Sound('Notification-sound.wav')
                correct_sound.play()
                # Move on to next question and add to score
                global_i += 1
                score_value += 1

            # If incorrect flag is hit
            else:
                incorrect_sound = mixer.Sound('Family feud-buzzer.wav')
                incorrect_sound.play()

            # Reset for next shot
            starY = 480
            star_state = "ready"
            flagX[i] = random.randint(0, 710)
            flagY[i] = random.randint(50, 150)

        # Reset flag location
        flag(flagX[i], flagY[i], i)

    # Star movement
    # If star completes launch, reset star
    if starY <= 0:
        starY = 480
        star_state = "ready"
    # If star is firing, move star
    if star_state == "fire":
        fire_star(starX, starY)
        starY -= starY_change

    # Update player position
    player(playerX, playerY)
    # Update score (if necessary)
    show_score(textX, textY)
    # Display question
    if global_i < 5:
        show_question(textX+150, textY)
    # Continuously update display
    pygame.display.update()