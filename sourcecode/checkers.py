########################################
# Author        : Ritvars Timermanis
# Matric No.    : 40298561
########################################

grid = [[-1]*8 for n in range(8)]

def clear():
    '''Clears the window by printing 30 blank lines'''
    for i in range(30):
        print "\n"

def main_menu():
    '''Display main menu'''
    while True:
        clear()
        print 20 * "#"
        print "Draughts v0.1"
        print 20 * "#"
        print " 1. Play"
        print " 2. About"
        print " 3. Quit"
        choice = input(">> ")
        return choice

if __name__ == "__main__":
    selection = main_menu()
    if selection == "1":
        print selection
    elif selection == "2":
        print selection
    elif selection == "3":
        exit()
    else:
        print "Invalid option. Please try again."
