from settings import *

#
#   REMEMBER! WHEN CALLING game_board, Y comes BEFORE X !!!
#


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
