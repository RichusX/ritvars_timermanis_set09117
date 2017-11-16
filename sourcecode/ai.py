import g # global vars
from random import choice
import piece as Piece
from copy import copy, deepcopy
from time import sleep

def pick_piece():
    '''
    Returns a random piece as a tuple that belongs to the AI and is movable.
    '''
    movable_pieces = []
    for y in range(8):
        for x in range(8):
            selected_piece = g.game_board[y][x]
            if selected_piece.startswith("X"):
                if len(Piece.availableMoves(x, y)[0]) is not 0:
                    movable_pieces.append((x, y))

    random = choice(movable_pieces)
    return random

def pick_destination(xOrigin, yOrigin):
    '''
    Picks a random destination for a piece at xOrigin, yOrigin
    '''
    movable_pieces_coords = []
    for i, (x,y) in enumerate(Piece.availableMoves(xOrigin, yOrigin)[2]):
        movable_pieces_coords.append(Piece.availableMoves(xOrigin, yOrigin)[2][i])
    random = choice(movable_pieces_coords)
    returnable = (random[1], random[0])
    return returnable
