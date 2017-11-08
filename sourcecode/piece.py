from settings import *

#
#   REMEMBER! WHEN CALLING game_board, Y comes BEFORE X !!!
#


def move(xOrigin, yOrigin, xDest, yDest):
    piece = game_board[xOrigin][yOrigin] # get the piece from origin
    game_board[xOrigin][yOrigin] = " " # set the origin to none
    game_board[xDest][yDest] = piece # set the destination to piece
    ''' '''
    if abs(xOrigin - xDest) == 2 and abs(yOrigin - yDest) == 2: # if piece moves by 2 tiles
        if (xOrigin > xDest) and (yOrigin > yDest): # IF jumping to TOP LEFT
            piece_jumped = game_board[yDest + 1][xDest + 1] # xDest + 1 and yDest + 1
            printCoords(xDest+1, yDest+1)
        elif (xOrigin < xDest) and (yOrigin < yDest): # IF jumping to BOTTOM RIGHT
            piece_jumped = game_board[yDest - 1][xDest - 1] # xDest - 1 and yDest - 1
            printCoords(xDest-1, yDest-1)
        elif (xOrigin > xDest) and (yOrigin < yDest): # IF jumping to BOTTOM LEFT
            piece_jumped = game_board[yDest - 1][xDest +1] # xDest + 1 and yDest - 1
            printCoords(xDest+1,yDest-1)
        elif (xOrigin < xDest) and (yOrigin > yDest): # IF jumping to TOP RIGHT
            piece_jumped = game_board[yDest + 1][xDest - 1] # xDest - 1 and yDest + 1
            printCoords(xDest-1, yDest+1)
        
    piece = game_board[yOrigin][xOrigin] # get the piece from origin
    game_board[yOrigin][xOrigin] = " " # set the origin to none
    game_board[yDest][xDest] = piece # set the destination to piece

    # TODO: Implement piece movement

def isValid(xOrigin, yOrigin):
    if game_board[xOrigin][yOrigin] is not " ": # Check if piece exists in the origin coordinates
        return True
    else:
        return False
def checkOwner(x, y):
    if game_board[y][x] == "X": # IF red team
        return "RED"
    elif game_board[y][x] == "O": # IF white team
        return "WHITE"
    else:
        return None

def printCoords(x, y):
    to_print = ""
    for key, value in INDEX.iteritems():
            if value == y:
                to_print += str(key)
    to_print += str(x)
    print(to_print)
