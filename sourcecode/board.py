from colorama import Style, Fore, Back
import g # Global variables

HEADER = '     0   1   2   3   4   5   6   7'
FOOTER = '   +---+---+---+---+---+---+---+---+'
SEPERATOR = '---------------------------------'

def print_board():
    print(HEADER)
    print(FOOTER)

    for y in range(0, 8):
        to_print = chr(y + 97).upper() + '  '
        for x in range(0, 9):
            if x <= 7 and y <= 7:
                if g.game_board[y][x] == "X":
                    to_print += '| ' + Fore.RED + "O" + Style.RESET_ALL + " "
                elif g.game_board[y][x] == "O":
                    to_print += '| ' + Fore.WHITE + "O" + Style.RESET_ALL + " "
                elif g.game_board[y][x] == "XX":
                    to_print += '| ' + Fore.RED + "X" + Style.RESET_ALL + " "
                elif g.game_board[y][x] == "OO":
                    to_print += '| ' + Fore.WHITE + "X" + Style.RESET_ALL + " "
                else:
                    to_print += '|   '
            else:
                    to_print += '|   '

        print(to_print)
        print(FOOTER)
    print("\n%s"% (SEPERATOR))
    print("Red Score: %s\nWhite score: %s" % (g.red_score, g.white_score))
    print("%s\n" % (SEPERATOR))
