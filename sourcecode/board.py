from colorama import Style, Fore
from global_vars import *

HEADER = '     0   1   2   3   4   5   6   7'
FOOTER = '   +---+---+---+---+---+---+---+---+'

def print_board():
    print(HEADER)
    print(FOOTER)

    for y in range(0, 8):
        to_print = chr(y + 97).upper() + '  '
        for x in range(0, 9):
            if x <= 7 and y <= 7:
                if game_board[y][x] == "X":
                    to_print += '| ' + Fore.RED + "O" + Fore.RESET + " "
                elif game_board[y][x] == "O":
                    to_print += '| ' + Fore.WHITE + "O" + Fore.RESET + " "
                else:
                    to_print += '|   '
            else:
                    to_print += '|   '

        print(to_print)
        print(FOOTER)
