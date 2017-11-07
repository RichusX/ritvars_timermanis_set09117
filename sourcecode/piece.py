from settings import *

def move(xOrigin, yOrigin, xDest, yDest):
    piece = game_board[xOrigin][yOrigin] # get the piece from origin
    game_board[xOrigin][yOrigin] = " " # set the origin to none
    game_board[xDest][yDest] = piece # set the destination to piece

    # TODO: Implement piece movement

def isValid(xOrigin, yOrigin):
    if game_board[xOrigin][yOrigin] is not " ": # Check if piece exists in the origin coordinates
        return True
    else:
        return False