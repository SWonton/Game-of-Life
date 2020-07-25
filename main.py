import numpy as np
import time

ON = 1
OFF = 0
VALUES = [ON, OFF]
ratio = [.5, .5]
width = int(input("Width:"))
height = int(input("Height:"))

def randomGrid(width,height):
    return np.random.choice(VALUES, width*height, p=ratio).reshape(width, height)

def deadGrid(width, height):
    return np.zeros((width,height))

def render(board):
    display = {
        OFF: ' ',
        ON: u"\u2588"
    }
    lines = []
    for y in range(0, height):
        line = '\n'
        for x in range(0, width):
            line += display[board[x][y]] * 2
        lines.append(line)
    print ( "|" + "|\n|".join(lines) + "|")

def nextCellState(cellCoord, board):
    x = cellCoord[0]
    y = cellCoord[1]
    liveNeighbors = 0
    for x1 in range((x-1), (x+1)):
        if x1 < 0: 
            x1 = width - 1
        elif x1 >= width:
            x1 = 0
        for y1 in range((y-1), (y+1)+1):
            if y1 < 0:
                y1 = height - 1
            if y1 >= height:
                y1 = 0

            if x1 == x and y1 == y: continue
            
            if board[x1][y1] == ON:
                liveNeighbors += 1
    if board[x][y] == ON:
        if liveNeighbors <= 1:
            return OFF
        elif liveNeighbors <= 3:
            return ON
        else:
            return OFF
    else:
        if liveNeighbors == 3:
            return ON
        else:
            return OFF

def nextBoardState(initBoard):
    nextBoard = deadGrid(width,height)
    for y in range(0, height):
        for x in range(0, width):
            nextBoard[x][y] = nextCellState((x,y), initBoard)
    return nextBoard

arr = randomGrid(width,height)
render(arr)
while True:
    arr = nextBoardState(arr)
    render(arr)
    time.sleep(1)
    