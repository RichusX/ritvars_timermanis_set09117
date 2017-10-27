import pygame
from pygame.locals import *

import os, math

version = "v0.1"

pygame.init()
pygame.font.init()

displayWidth = 560
displayHeight = 560

grid = [ [-1]*8  for n in range(8)]
cellWidth = 70

colour = {"red":(255,0,0), "green":(0,255,0), "blue":(0,0,255), "white": (255,255,255), "black":(0,0,0)}

redPiece = pygame.image.load("img/red.png")
whitePiece = pygame.image.load("img/white.png")

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Draughts %s" % (version))
clock = pygame.time.Clock()

finished = False

def isOdd(x):
    return bool(x-((x>>1)<<1))

def intro():
    font = pygame.font.SysFont('Segoe UI', 30)

    gameDisplay.fill(colour["white"])
    textSurface = font.render('Draughts', 1, (0, 0, 0))
    gameDisplay.blit(textSurface, ((displayWidth/2), (displayHeight/2)))
    pygame.display.update()
    clock.tick(120)

def drawBoard():
    x,y = 0,0
    #pygame.draw.rect(gameDisplay, (colour["blue"]), Rect((560, 0), (200, 560)))
    for xrow, row in enumerate(grid):
        for xcol, col in enumerate(row):
            if isOdd(xrow+xcol):
                pygame.draw.rect(gameDisplay, (colour["white"]), Rect((x,y), (cellWidth, cellWidth)))
                if xrow < 3:
                    gameDisplay.blit(whitePiece, (x,y))
                elif xrow > 4:
                    gameDisplay.blit(redPiece, (x,y))
            else:
                pygame.draw.rect(gameDisplay, (colour["black"]), Rect((x,y), (cellWidth, cellWidth)))
            x = x + cellWidth
        y = y + cellWidth
        x = 0


class Game:
    def __init__(self):
        self.board = drawBoard()


class Piece:
    def __init__(self, colour, king = False):
        self.colour = colour
        self.king = king

if __name__ == "__main__":
    intro()
    drawBoard()

    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            print(event)
        pygame.display.update()
        clock.tick(60)

pygame.quit()
quit()
