import g # Global variables
from checkers import print_error

#
#   REMEMBER! WHEN CALLING game_board, Y comes BEFORE X !!!
#


def move(xOrigin, yOrigin, xDest, yDest):
    '''
    Function resposible for moving the piece

    TODO: King logic
    TODO: 
    '''
   
    if (xOrigin > xDest) and (yOrigin > yDest): # IF moving to TOP LEFT
        if (checkOwner(xOrigin, yOrigin) == "RED") and not checkKing(xOrigin, yOrigin): # IF team red
            print_error("Error. Only a king can move backwards.")
            return False
        
        if abs(xOrigin - xDest) == 2 and abs(yOrigin - yDest) == 2: # if piece moves by 2 tiles (jumps)
            # xDest + 1 and yDest + 1
            if jumpCheck(xOrigin, yOrigin, xDest, yDest, True, True) is False:
                return False
        elif (abs(xOrigin - xDest) > 2 or abs(yOrigin - yDest) > 2) or abs(xOrigin - xDest) is not abs(yOrigin - yDest):
            print_error("Error. Invalid movement.")
            return False

    elif (xOrigin < xDest) and (yOrigin < yDest): # IF moving to BOTTOM RIGHT
        if (checkOwner(xOrigin, yOrigin) == "WHITE") and not checkKing(xOrigin, yOrigin): # IF team red
            print_error("Error. Only a king can move backwards.")
            return False

        if abs(xOrigin - xDest) == 2 and abs(yOrigin - yDest) == 2: # if piece moves by 2 tiles (jumps)
            # xDest - 1 and yDest - 1
            if jumpCheck(xOrigin, yOrigin, xDest, yDest, False, False) is False:
                return False
        elif (abs(xOrigin - xDest) > 2 or abs(yOrigin - yDest) > 2) or abs(xOrigin - xDest) is not abs(yOrigin - yDest):
            print_error("Error. Invalid movement.")
            return False

    elif (xOrigin > xDest) and (yOrigin < yDest): # IF moving to BOTTOM LEFT
        if (checkOwner(xOrigin, yOrigin) == "WHITE") and not checkKing(xOrigin, yOrigin): # IF team red
            print_error("Error. Only a king can move backwards.")
            return False

        if abs(xOrigin - xDest) == 2 and abs(yOrigin - yDest) == 2: # if piece moves by 2 tiles (jumps)
            # xDest + 1 and yDest - 1
            if jumpCheck(xOrigin, yOrigin, xDest, yDest, True, False) is False:
                return False
        elif (abs(xOrigin - xDest) > 2 or abs(yOrigin - yDest) > 2) or abs(xOrigin - xDest) is not abs(yOrigin - yDest):
            print_error("Error. Invalid movement.")
            return False

    elif (xOrigin < xDest) and (yOrigin > yDest): # IF moving to TOP RIGHT
        if (checkOwner(xOrigin, yOrigin) == "RED") and not checkKing(xOrigin, yOrigin): # IF team red
            print_error("Error. Only a king can move backwards.")
            return False
            
        if abs(xOrigin - xDest) == 2 and abs(yOrigin - yDest) == 2: # if piece moves by 2 tiles (jumps)
            # xDest - 1 and yDest + 1
            if jumpCheck(xOrigin, yOrigin, xDest, yDest, False, True) is False:
                return False
        elif (abs(xOrigin - xDest) > 2 or abs(yOrigin - yDest) > 2) or abs(xOrigin - xDest) is not abs(yOrigin - yDest):
            print_error("Error. Invalid movement.")
            return False
    else:
        print_error("Error. You can only move your piece diognaly.")
        return False
        
    piece = g.game_board[yOrigin][xOrigin] # get the piece from origin
    g.game_board[yOrigin][xOrigin] = " " # set the origin to empty
    g.game_board[yDest][xDest] = piece # set the destination to piece

    return True

def exists(xOrigin, yOrigin):
    if g.game_board[yOrigin][xOrigin] is not " ": # Check if piece exists in the origin coordinates
        return True
    else:
        return False

def checkOwner(x, y):
    if g.game_board[y][x] == "X" or g.game_board[y][x] == "XX": # IF red team
        return "RED"
    elif g.game_board[y][x] == "O" or g.game_board[y][x] == "OO": # IF white team
        return "WHITE"
    else:
        return None

def checkKing(x, y):
    if g.game_board[y][x] == "XX" or g.game_board[y][x] == "OO":
        return True
    else:
        return False

def printCoords(x, y):
    to_print = ""
    for key, value in g.INDEX.iteritems():
        if value == y:
            to_print += str(key)
            break # stop the loop as the correct key has been found
    to_print += str(x)
    print(to_print)

def jumpCheck(xOrigin, yOrigin, xDest, yDest, addition1, addition2):
    if checkKing(xOrigin, yOrigin): # if king
        x_movement = abs(xOrigin - xDest)
        y_movement = abs(yOrigin - yDest)
        if x_movement != y_movement:
            print_error("What the fuck is going on") # DONT LEAVE THIS IN!!!
            return False
        else:
            movement = x_movement # Doesn't matter if we take x or y movement as they should be the same at this point
            for i in range(movement):
                i = i + 1 # otherwise counting will be off by 1
                if (addition1 and addition2): # IF moving to TOP LEFT
                    x = xDest + i
                    y = yDest + i
                elif (not addition1 and not addition2): # IF moving to BOTTOM RIGHT
                    x = xDest - i
                    y = yDest - i
                elif (addition1 and not addition2): # IF moving to BOTTOM LEFT
                    x = xDest + i
                    y = yDest - i
                elif (not addition1 and addition2): # IF moving to TOP RIGHT
                    x = xDest - i
                    y = yDest + i
                if i == 1:
                    if checkOwner(x, y) != None:
                        pass
                if checkOwner(x, y) == None:
                    pass

    else: # if not king
        if (addition1 and addition2): # IF moving to TOP LEFT
            x = xDest + 1
            y = yDest + 1
        elif (not addition1 and not addition2): # IF moving to BOTTOM RIGHT
            x = xDest - 1
            y = yDest - 1
        elif (addition1 and not addition2): # IF moving to BOTTOM LEFT
            x = xDest + 1
            y = yDest - 1
        elif (not addition1 and addition2): # IF moving to TOP RIGHT
            x = xDest - 1
            y = yDest + 1

        if (checkOwner(x, y) == "WHITE" and g.white_turn) or (checkOwner(x, y) == "RED" and not g.white_turn):
            print_error("Error. You can't jump over your own piece.")
            return False
        elif checkOwner(x, y) == None:
            print_error("Error. You can't jump over an empty tile.")
            return False
        else:
            g.game_board[y][x] = " "
            if g.white_turn:
                g.white_score += 1
            else:
                g.red_score += 1

def availableMoves(x, y):
    available_moves = []
    available_moves_coords = []
    available_actions = {"move":False, "jump":False}
    surr_tiles = {"top_left": None, "top_right": None, "bottom_left": None, "bottom_right": None}
    surr_tiles_coords = {"top_left": (None, None), "top_right": (None, None), "bottom_left": (None, None), "bottom_right": (None, None)}
    surr_jumps = {"top_left": None, "top_right": None, "bottom_left": None, "bottom_right": None}
    surr_jumps_coords = {"top_left": (None, None), "top_right": (None, None), "bottom_left": (None, None), "bottom_right": (None, None)}

    if not checkKing(x, y):  # IF NOT king
        # Check surrounding tiles
        surr_tiles["top_left"] = calculate_nearby(x, y, 0, 1)[0]
        surr_tiles_coords["top_left"] = calculate_nearby(x, y, 0, 1)[1]
        surr_tiles["top_right"] = calculate_nearby(x, y, 1, 1)[0]
        surr_tiles_coords["top_right"] = calculate_nearby(x, y, 1, 1)[1]
        surr_tiles["bottom_left"] = calculate_nearby(x, y, 2, 1)[0]
        surr_tiles_coords["bottom_left"] = calculate_nearby(x, y, 2, 1)[1]
        surr_tiles["bottom_right"] = calculate_nearby(x, y, 3, 1)[0]
        surr_tiles_coords["bottom_right"] = calculate_nearby(x, y, 3, 1)[1]

        # Check surrounding jumps
        surr_jumps["top_left"] = calculate_nearby(x, y, 0, 2)[0]
        surr_jumps_coords["top_left"] = calculate_nearby(x, y, 0, 2)[1]
        surr_jumps["top_right"] = calculate_nearby(x, y, 1, 2)[0]
        surr_jumps_coords["top_right"] = calculate_nearby(x, y, 1, 2)[1]
        surr_jumps["bottom_left"] = calculate_nearby(x, y, 2, 2)[0]
        surr_jumps_coords["bottom_left"] = calculate_nearby(x, y, 2, 2)[1]
        surr_jumps["bottom_right"] = calculate_nearby(x, y, 3, 2)[0]
        surr_jumps_coords["bottom_right"] = calculate_nearby(x, y, 3, 2)[1]

        for key, value in surr_tiles.iteritems():
            if value != None:
                if (key not in ['bottom_left', 'bottom_right'] and g.white_turn) or (key not in ['top_left', 'top_right'] and not g.white_turn):
                    if (value.startswith("X") and g.white_turn) or (value.startswith("O") and not g.white_turn): # Check if the piece there can be jumped
                        if surr_jumps[key] == " ": # Check if there's a piece behind it
                            available_moves.append("Can jump to %s" % (str(key).replace("_", " ")))
                            available_moves_coords.append(surr_jumps_coords[key])
                            available_actions["jump"] = True
                    elif value == " ": # If surrounding tile empty then the piece can be moved there
                        available_moves.append("Cam move to %s" % (str(key).replace("_", " ")))
                        available_moves_coords.append(surr_tiles_coords[key])
                        available_actions["move"] = True
    else: # IF king
        surr_tiles_KING = {"top_left": 8*[None], "top_right": 8*[None], "bottom_left": 8*[None], "bottom_right": 8*[None]}
        surr_tiles_KING_coords = {"top_left": 8*(None, None), "top_right": 8*(None, None), "bottom_left": 8*(None, None), "bottom_right": 8*(None, None)}
        keys = ["top_left", "top_right", "bottom_left", "bottom_right"]

        i = 1
        while i <= 8: # Gather 8 pieces in all for directions

            surr_tiles_KING["top_left"][i-1] = calculate_nearby(x, y, 0, i)[0]
            surr_tiles_KING_coords["top_left"][i-1] = calculate_nearby(x, y, 0, i)[1]
            surr_tiles_KING["top_right"][i-1] = calculate_nearby(x, y, 1, i)[0]
            surr_tiles_KING_coords["top_right"][i-1] = calculate_nearby(x, y, 1, i)[1]
            surr_tiles_KING["bottom_left"][i-1] = calculate_nearby(x, y, 2, i)[0]
            surr_tiles_KING_coords["bottom_left"][i-1] = calculate_nearby(x, y, 2, i)[1]
            surr_tiles_KING["bottom_right"][i-1] = calculate_nearby(x, y, 3, i)[0]
            surr_tiles_KING_coords["bottom_right"][i-1] = calculate_nearby(x, y, 3, i)[1]

            i += 1 # add 1 to counter
        
        for direction in range(4): # Loops 4 times, once for each direction
            for idx, value in enumerate(surr_tiles_KING[keys[direction]]):
                if value == None: # Stop once reached end of board
                    break
                elif (str(value).startswith("X") and g.white_turn) or (str(value).startswith("O") and not g.white_turn):
                    target_piece = calculate_nearby(x, y, direction, idx)[0]
                    if (target_piece.startswith("X") and g.white_turn) or (target_piece.startswith("O") and not g.white_turn):
                        behind_target = calculate_nearby(x, y, direction, idx+1)[0]
                        if behind_target == " ": # check if tile behind the target piece is empty
                            available_moves.append("Can jump to %s" % (str(keys[direction]).replace("_", " ")))
                            available_moves_coords.append(surr_tiles_KING_coords[direction])
                            available_actions["jump"] = True
            
            if calculate_nearby(x, y, direction, 1)[0] == " ":
                available_moves.append("Can move to %s" % (str(keys[direction]).replace("_", " ")))
                available_moves_coords.append(surr_tiles_KING_coords[direction])
                available_actions["move"] = True

    return [available_moves, available_actions, available_moves_coords]

def calculate_nearby(x, y, direction=0, distance=0):
    result = None
    result_coords = (None, None)
    if direction == 0:
        try:
            if (x-distance) < 0 or (y-distance) < 0:
                result = None
            else:
                result = g.game_board[y-distance][x-distance]
                result_coords = (y-distance, x-distance)
        except:
            result = None
    elif direction == 1:
        try:
            if (x+distance) < 0 or (y-distance) < 0:
                result = None
            else:
                result = g.game_board[y-distance][x+distance]
                result_coords = (y-distance, x+distance)
        except:
            result = None
    elif direction == 2:
        try:
            if (x-distance) < 0 or (y+distance) < 0:
                result = None
            else:
                result = g.game_board[y+distance][x-distance]
                result_coords = (y+distance, x-distance)
        except:
            result = None
    elif direction == 3:
        try:
            if (x+distance) < 0 or (y+distance) < 0:
                result = None
            else:
                result = g.game_board[y+distance][x+distance]
                result_coords = (y+distance, x+distance)
        except:
            result = None

    return (result, result_coords)
