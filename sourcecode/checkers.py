########################################
# Author        : Ritvars Timermanis
# Matric No.    : 40298561
########################################

import time
import re
from colorama import Fore, Style, Back, init
import board as Board
import piece as Piece
from settings import *

def clear():
    '''Clears the window by printing 30 blank lines'''
    for i in range(30):
        print "\n"


def main_menu():
    '''Display main menu'''
    while True:
        clear()
        print 20 * "-"
        print "Checkers %s" % (VERSION)
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
    print "Checkers %s" % (VERSION)
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


def play_pvp():
    coordinates_re = re.compile(r'^(?:[a-hA-H]{1})(?:[0-7]){1}$', flags=re.IGNORECASE) # Check for valid coordinates using regular expressions (aka regex)

    finished = False
    while not finished:
        print_board()
        while True:
            origin_coordinates = raw_input("Enter the piece you want to move e.g. \"F2\"\n>>")
            if not re.match(coordinates_re, origin_coordinates):
                print_error("Error. Invalid input.")
            else:
                xOrigin = int(origin_coordinates[1])
                yOrigin = INDEX[origin_coordinates[0].upper()]
                if Piece.isValid(xOrigin, yOrigin):
                    if (Piece.checkOwner(xOrigin, yOrigin) == "WHITE") and not white_turn or (Piece.checkOwner(xOrigin, yOrigin) == "RED") and white_turn: # Check if moving the correct teams piece
                        print_error("Error. You can only move a piece that belongs to you.")
                    else:
                        break
                else:
                    print_error("Error. Invalid piece selected.")
        # TODO: check if the piece selected belongs to the player

        while True:
            destination_coordinates = raw_input("Enter the corrdinates for the tile you want to move the piece to\n>>")
            if not re.match(coordinates_re, destination_coordinates):
                print_error("Error! Invalid input.")
            else:
                if destination_coordinates == origin_coordinates: # Make sure that both coordinates are actually different from each other
                    print("Destination coordinates need to be different than the origin coordinates!") 
                else:
                    xDest = int(destination_coordinates[1])
                    yDest = INDEX[destination_coordinates[0].upper()]
                    break
        # TODO: Check if it's a legal move before moving
        Piece.move(xOrigin, yOrigin, xDest, yDest)


def play_ai():
    # TODO: Implement playing vs an AI
    pass


if __name__ == "__main__":
    init(convert=True)
    while True:
        selection = main_menu()
        if selection == "1":
            play_pvp()
        elif selection == "2":
            print "Play with AI"
            time.sleep(2)
        elif selection == "3":
            about_screen()
        elif selection == "4":
            exit("Exiting...")
        else:
            print_error("Invalid option. Please try again.")
            time.sleep(2)
