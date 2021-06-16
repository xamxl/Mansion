import pygame
import random
import math

#hi this is me

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("The Greenhouse")

playerX = 385
playerY = 285
playerX_change = 0
playerY_change = 0

chance = 10000

leakX = [random.randint(10, 790)]
leakY = [random.randint(10, 590)]
leak_radius = [15]
leak_green = [0]

def player_draw(x, y):
    pygame.draw.rect(screen, (100, 0, 0), pygame.Rect(x, y, 15, 15))

def leak_draw(x, y, r, g):
    pygame.draw.circle(screen, (0, g, 100), (x, y), r, 1)

def collision_check(playerX, playerY, leakX, leakY, i):
    distance = math.sqrt(math.pow(playerX - leakX, 2) + math.pow(playerY - leakY, 2))
    if distance < 20:
        return True
    else:
        return False

running = True
while running:

    if random.randint(0, chance) == 1:
        leakX.append(random.randint(10, 790))
        leakY.append(random.randint(10, 590))
        leak_radius.append(15)
        leak_green.append(0)


    screen.fill((0, 50, 50))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1
            if event.key == pygame.K_UP:
                playerY_change = -0.1
            if event.key == pygame.K_DOWN:
                playerY_change = 0.1
            if event.key == pygame.K_SPACE:
                for i in range(len(leakX)):
                    if collision_check(playerX, playerY, leakX[i], leakY[i], i):
                        leakX.pop(i)
                        leakY.pop(i)
                        leak_radius.pop(i)
                        if chance > 1000:
                            chance = chance - 100
                        break

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    for i in range(len(leakX)):
        if leak_radius[i] < 100:
            leak_radius[i] += 0.05
            leak_green[i] += 0.025
        else:
            leak_radius[i] = 15
            leak_green[i] = 0
        leak_draw(leakX[i], leakY[i], leak_radius[i], leak_green[i])

    playerX += playerX_change
    playerY += playerY_change
    player_draw(playerX, playerY)

    if playerX <= 15:
        playerX = 15
    elif playerX >= 775:
        playerX = 775

    if playerY <= 15:
        playerY = 15
    elif playerY >= 575:
        playerY = 575

    pygame.display.update()
