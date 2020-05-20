import pygame
import numpy as np
import time

pygame.init()

ancho, alto = 580, 580
screen = pygame.display.set_mode((ancho, alto))

bg = 25, 25, 25
screen.fill(bg)

celdasX, celdasY = 50, 50

dimCeldaX = ancho / celdasX
dimCeldaY = alto / celdasY

gameState = np.zeros((celdasX, celdasY))


pauseExcect = True

while 1:

    newGS = np.copy(gameState)
    screen.fill(bg)
    time.sleep(0.1)
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.KEYDOWN:
            pauseExcect= not pauseExcect
        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            clickX, clickY = int(np.floor(posX/dimCeldaX)), int(np.floor(posY/dimCeldaY))
            newGS[clickX,clickY] = not mouseClick[2]

    for y in range(0, celdasX):
        for x in range(0, celdasY):
            if not pauseExcect:

                computoVecinos = gameState[(x - 1) % celdasX, (y - 1) % celdasY] + \
                                 gameState[(x) % celdasX, (y - 1) % celdasY] + \
                                 gameState[(x + 1) % celdasX, (y - 1) % celdasY] + \
                                 gameState[(x - 1) % celdasX, (y) % celdasY] + \
                                 gameState[(x + 1) % celdasX, (y) % celdasY] + \
                                 gameState[(x - 1) % celdasX, (y + 1) % celdasY] + \
                                 gameState[(x) % celdasX, (y + 1) % celdasY] + \
                                 gameState[(x + 1) % celdasX, (y + 1) % celdasY]

                if gameState[x, y] == 0 and computoVecinos == 3:
                    newGS[x, y] = 1
                elif gameState[x, y] == 1 and (computoVecinos < 2 or computoVecinos > 3):
                    newGS[x, y] = 0

            poly = [(x*dimCeldaX,y*dimCeldaY),
                    ((x+1)*dimCeldaX,y*dimCeldaY),
                    ((x+1)*dimCeldaX,(y+1)*dimCeldaY),
                    (x*dimCeldaX,(y+1)*dimCeldaY)]

            if newGS[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    gameState = np.copy(newGS)
    pygame.display.flip()
