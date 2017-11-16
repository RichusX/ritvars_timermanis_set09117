
# Legend
# X - Red piece
# O - White piece
# XX - Red king
# OO - White king

# game_board = [
#     [" ", "X", " ", "X", " ", " ", " ", "X"],
#     ["X", " ", " ", " ", "X", " ", "X", " "],
#     [" ", " ", " ", "X", " ", " ", " ", "X"],
#     [" ", " ", "OO", " ", " ", " ", "O", " "],
#     [" ", " ", " ", " ", " ", "X", " ", " "],
#     ["O", " ", "O", " ", " ", " ", "O", " "],
#     [" ", "O", " ", "O", " ", "O", " ", "O"],
#     ["O", " ", "O", " ", "O", " ", "O", " "]
# ] # game_board[Y][X] because 2D arrays ;-;

game_board = [
    [" ", "X", " ", "X", " ", "X", " ", "X"],
    ["X", " ", "X", " ", "X", " ", "X", " "],
    [" ", "X", " ", "X", " ", "X", " ", "X"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["O", " ", "O", " ", "O", " ", "O", " "],
    [" ", "O", " ", "O", " ", "O", " ", "O"],
    ["O", " ", "O", " ", "O", " ", "O", " "]
]

INDEX = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7}
VERSION = "v1.0"

white_turn = True # Default to true, as white team starts first

white_score = 0 # White team score
red_score = 0 # Red team score