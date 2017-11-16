########################################
# Author        : Ritvars Timermanis
# Matric No.    : 40298561
########################################

import g # Global variables
import time
import re
from colorama import Fore, Style, Back, init
from copy import copy, deepcopy
import board as Board
import piece as Piece
import ai


def clear():
    '''Clears the window by printing 30 blank lines'''
    for i in range(30):
        print "\n"


def main_menu():
    '''Display main menu'''
    while True:
        clear()
        print 20 * "-"
        print "Checkers %s" % (g.VERSION)
        print 20 * "-"
        print " 1. Play\n" \
              " 2. Play with AI\n" \
              " 3. About\n" \
              " 4. Exit"
        return raw_input(">> ")


def about_screen():
    '''Display about screen'''
    clear()
    print 20 * "-"
    print "Checkers %s" % (g.VERSION)
    print 20 * "-"
    print "Developed by Ritvars Timermanis\n" \
          "Version 0.1\n" \
          "If you encounter any issues please send me an e-mail at me@richusx.me\n\n" \
          "Press any key to return to main menu..."
    raw_input()


def print_board():
    clear()
    Board.print_board()

def print_error(msg):
    print(Fore.WHITE + Back.RED + str(msg) + Style.RESET_ALL)

def finished_screen(winner):
    clear()
    print(Fore.GREEN + \
          " _____ _____ _____ _____    _____ _____ _____ _____ \n"\
          "|   __|  _  |     |   __|  |     |  |  |   __| __  |\n"\
          "|  |  |     | | | |   __|  |  |  |  |  |   __|    -|\n"\
          "|_____|__|__|_|_|_|_____|  |_____|\___/|_____|__|__|\n" + Style.RESET_ALL)
    print("\n  CONGRATS, %s TEAM! YOU WON!" % (winner))
    raw_input("\n\n\nPress any key to return to menu...")

def play(play_with_ai=False):
    coordinates_re = re.compile(r'^(?:[a-hA-H]{1})(?:[0-7]){1}$', flags=re.IGNORECASE) # Check for valid input coordinates using regex

    winner = ""
    skip_origin = False # don't ask for origin coords as the player can jump another piece
    previous_dest = "" # previous destination entered (for multiple jumps)
    undo_board = deepcopy(g.game_board)
    undo_score = (0, 0)
    undo_turn = False

    xOrigin = 0
    yOrigin = 0
    xDest = 0
    yDest = 0

    finished = False # game status
    while not finished:
        # Track kings
        for x in range(8):
            if (Piece.checkOwner(x, 0) == "WHITE") and (g.game_board[0][x] == "O"): # If WHITE piece made it to the other side then set it to king
                g.game_board[0][x] = "OO"
            elif (Piece.checkOwner(x, 7) == "RED") and (g.game_board[7][x] == "X"): # If RED piece made it to the other side then set it to king
                g.game_board[0][x] = "XX"

        if play_with_ai:
            if g.white_turn:
                ai_turn = False
            else:
                ai_turn = True
        else:
            ai_turn = False

        # Track how many pieces left on board
        white_left = 0
        red_left = 0
        for y in range(8):
            for x in range(8):
                if g.game_board[y][x].startswith("O"):
                    white_left += 1
                elif g.game_board[y][x].startswith("X"):
                    red_left += 1

        # Stop the game if either of the teams have no pieces left
        if white_left == 0:
            winner = "RED"
            finished = True
        elif red_left == 0:
            winner = "WHITE"
            finished = True

        reset_turn = False
        undo = False
        print_board()

        if undo_turn:
            g.white_turn = not g.white_turn
            undo_turn = False

        origin_loop = True # Both loops active by default unless other specified
        dest_loop = True

        while origin_loop:
            if g.white_turn:
                piece_hint = Fore.WHITE + "O" + Style.RESET_ALL
            else:
                piece_hint = Fore.RED + "O" + Style.RESET_ALL

            if not skip_origin:
                if not ai_turn:
                    origin_coordinates = raw_input("Enter the piece you want to move [%s] \n>>" % (piece_hint))
                else:
                    origin_coordinates = ai.pick_piece()
            else:
                origin_coordinates = previous_dest

            if not ai_turn:
                regex_valid = re.match(coordinates_re, origin_coordinates)
            else:
                regex_valid = True

            if origin_coordinates == "undo" and not ai_turn:
                g.game_board = deepcopy(undo_board)
                g.white_score = undo_score[0]
                g.red_score = undo_score[1]
                undo = True
                undo_turn = True
                dest_loop = False
                origin_loop = False
            elif not regex_valid:
                print_error("Error. Invalid input.")
                time.sleep(2)
            else:
                if ai_turn:
                    xOrigin = origin_coordinates[0]
                    yOrigin = origin_coordinates[1]
                else:
                    xOrigin = int(origin_coordinates[1])
                    yOrigin = g.INDEX[origin_coordinates[0].upper()]
                availabe_moves = Piece.availableMoves(xOrigin, yOrigin)[0]
                if Piece.exists(xOrigin, yOrigin):
                    if (Piece.checkOwner(xOrigin, yOrigin) == "WHITE") and not g.white_turn or (Piece.checkOwner(xOrigin, yOrigin) == "RED") and g.white_turn: # Check if moving the correct teams piece
                        print_error("Error. You can only move a piece that belongs to you.")
                    elif len(availabe_moves) is not 0:
                        print(Board.SEPERATOR)
                        for move in availabe_moves:
                            print(move)
                        print(Board.SEPERATOR)
                        break
                    else:
                        print_error("Error. Invalid piece selected.")
                else:
                    print_error("Error. Invalid piece selected.")

        while dest_loop:
            if not ai_turn:
                destination_coordinates = raw_input("Enter the corrdinates for the tile you want to move the piece to\n>>")
                previous_dest = destination_coordinates
                regex_valid = re.match(coordinates_re, destination_coordinates)
            else:
                destination_coordinates = ai.pick_destination(xOrigin, yOrigin)
                for key, value in g.INDEX.iteritems():
                    if value == destination_coordinates[1]:
                        previous_dest += str(value)
                previous_dest += str(destination_coordinates[0])
                regex_valid = True

            if destination_coordinates == "cancel" and not ai_turn:
                reset_turn = True
                break
            elif not regex_valid:
                print_error("Error! Invalid input.")
            else:
                if destination_coordinates == origin_coordinates: # Make sure that both coordinates are actually different from each other
                    print("Destination coordinates need to be different than the origin coordinates!") 
                else:
                    if ai_turn:
                        xDest = destination_coordinates[0]
                        yDest = destination_coordinates[1]
                    else:
                        xDest = int(destination_coordinates[1])
                        yDest = g.INDEX[destination_coordinates[0].upper()]
                    
                    if g.game_board[yDest][xDest] is not " ":
                        print_error("Error. Invalid movement.")
                    else:
                        break # exit loop

        if (not reset_turn) and (not undo): # TODO: LEFT OFF HERE, UNDO NO WORKY
            points_before = [g.white_score, g.red_score]
            undo_board_pre = deepcopy(g.game_board)
            undo_score_pre = (g.white_score, g.red_score)
            if Piece.move(xOrigin, yOrigin, xDest, yDest):
                undo_board = undo_board_pre
                undo_score = undo_score_pre
                points_after = [g.white_score, g.red_score]
                if points_before == points_after:
                    g.white_turn = not g.white_turn # Hand over turn to other team (as no piece was jumped (as the score didn't change))
                    skip_origin = False
                else:
                    if len(Piece.availableMoves(xDest, yDest)[0]) is 0:
                        g.white_turn = not g.white_turn # Hand over turn to other team because no other moves can be made
                        skip_origin = False
                    else:
                        can_jump = Piece.availableMoves(xDest, yDest)[1]["jump"]
                        if can_jump:
                            skip_origin = True
                        else:
                            skip_origin = False
                            g.white_turn = not g.white_turn # Hand over turn to other team because no other moves can be made
            else:
                time.sleep(2) # Wait for 2 seconds so the player can read the error message.
    if finished:
        finished_screen(winner)

if __name__ == "__main__":
    init(convert=True)
    while True:
        selection = main_menu()
        if selection == "1":
            play()
        elif selection == "2":
            play(True)
            time.sleep(2)
        elif selection == "3":
            about_screen()
        elif selection == "4":
            exit("Exiting...")
        else:
            print_error("Invalid option. Please try again.")
            time.sleep(2)
