import numpy as np
import pygame, sys
import time

ON = 1
OFF = 0
VALUES = [ON, OFF]
ratio = [.5, .5]
#width = int(input("Width:"))
#height = int(input("Height:"))
width = 20
height = 20
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400

def randomGrid(width,height):
    return np.random.choice(VALUES, width*height, p=ratio).reshape(width, height)

def deadGrid(width, height):
    return np.zeros((width,height))

def nextCellState(cellCoord, board):
    x = cellCoord[0]
    y = cellCoord[1]
    liveNeighbors = 0
    x2 = 0
    y2 = 0
    for x1 in range((x-1), (x+2)):
        if x1 < 0: 
            x2 = width - 1
        elif x1 >= width:
            x2 = 0
        else:
            x2 = x1
        for y1 in range((y-1), (y+2)):
            if y1 < 0:
                y2 = height - 1
            if y1 >= height:
                y2 = 0
            else:
                y2 = y1

            if x1 == x and y1 == y: continue
            
            if board[x2][y2] == 1:
                liveNeighbors += 1
    if board[x][y] == 1:
        if liveNeighbors == 3 or liveNeighbors == 2:
            return 1
        else:
            return 0
    else:
        if liveNeighbors == 3:
            return 1
        else:
            return 0

def nextBoardState(initBoard):
    nextBoard = deadGrid(width,height)
    for y in range(0, height):
        for x in range(0, width):
            nextBoard[x][y] = nextCellState((x,y), initBoard)
    return nextBoard

def main(arr):
    global SCREEN, CLOCK
    pygame.init()
    pygame.display.set_caption('Game of Life')

    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:
        drawGrid(arr)
        time.sleep(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        arr = nextBoardState(arr)


def drawGrid(board):
    display = {
        OFF: (0,0,0),
        ON: (200,200,200)
    }
    blockSize = 20 #Set the size of the grid block
    for x in range(height):
        for y in range(width):
            rect = pygame.Rect(x*blockSize, y*blockSize,
                               blockSize, blockSize)
            pygame.draw.rect(SCREEN, display[board[x - 1][y - 1]], rect, 0)

arr = randomGrid(width,height)

main(arr)
    