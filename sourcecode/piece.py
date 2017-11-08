import global_vars
from checkers import print_error

#
#   REMEMBER! WHEN CALLING game_board, Y comes BEFORE X !!!
#


def move(xOrigin, yOrigin, xDest, yDest):
    '''
    Function resposible for moving the piece

    TODO: Count the score
    TODO: Track which teams turn it is
    '''
    if global_vars.white_turn: # Store the score before the piece move in a seperate variable
        score_before = global_vars.white_score
    else:
        score_before = global_vars.red_score

    if abs(xOrigin - xDest) == 2 and abs(yOrigin - yDest) == 2: # if piece moves by 2 tiles (jumps)
        if (xOrigin > xDest) and (yOrigin > yDest): # IF jumping to TOP LEFT
            piece_jumped = global_vars.game_board[yDest + 1][xDest + 1] # xDest + 1 and yDest + 1
            if (checkOwner(xDest+1, yDest+1) == "WHITE" and not global_vars.white_turn) or (checkOwner(xDest+1, yDest+1) == "RED" and global_vars.white_turn):
                print_error("Error. You can't jump over your own piece.")
                return False

        elif (xOrigin < xDest) and (yOrigin < yDest): # IF jumping to BOTTOM RIGHT
            piece_jumped = global_vars.game_board[yDest - 1][xDest - 1] # xDest - 1 and yDest - 1
            if (checkOwner(xDest-1, yDest-1) == "WHITE" and not global_vars.white_turn) or (checkOwner(xDest-1, yDest-1) == "RED" and global_vars.white_turn):
                print_error("Error. You can't jump over your own piece.")
                return False

        elif (xOrigin > xDest) and (yOrigin < yDest): # IF jumping to BOTTOM LEFT
            piece_jumped = global_vars.game_board[yDest - 1][xDest +1] # xDest + 1 and yDest - 1
            checkOwner(xDest+1,yDest-1)
            if (checkOwner(xDest+1,yDest-1) == "WHITE" and not global_vars.white_turn) or (checkOwner(xDest+1,yDest-1) == "RED" and global_vars.white_turn):
                print_error("Error. You can't jump over your own piece.")
                return False

        elif (xOrigin < xDest) and (yOrigin > yDest): # IF jumping to TOP RIGHT
            piece_jumped = global_vars.game_board[yDest + 1][xDest - 1] # xDest - 1 and yDest + 1
            if (checkOwner(xDest-1, yDest+1) == "WHITE" and not global_vars.white_turn) or (checkOwner(xDest-1, yDest+1) == "RED" and global_vars.white_turn):
                print_error("Error. You can't jump over your own piece.")
                return False
        
    piece = global_vars.game_board[yOrigin][xOrigin] # get the piece from origin
    global_vars.game_board[yOrigin][xOrigin] = " " # set the origin to none
    global_vars.game_board[yDest][xDest] = piece # set the destination to piece

    return True

    # TODO: Implement piece movement

def exists(xOrigin, yOrigin):
    if global_vars.game_board[yOrigin][xOrigin] is not " ": # Check if piece exists in the origin coordinates
        return True
    else:
        return False

def checkOwner(x, y):
    if global_vars.game_board[y][x] == "X": # IF red team
        return "RED"
    elif global_vars.game_board[y][x] == "O": # IF white team
        return "WHITE"
    else:
        return None

def printCoords(x, y):
    to_print = ""
    for key, value in global_vars.INDEX.iteritems():
            if value == y:
                to_print += str(key)
                break # stop the loop as the correct key has been found
    to_print += str(x)
    print(to_print)
