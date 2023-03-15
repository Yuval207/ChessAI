"""
This file is the engine file which will be responsible for storing information about the current state of chess game
and also will be responsible for determining the valid moves at the current state while keeping a move log.
"""

class GameState():
    def __init__(self):
        #board is an 8X8 2d list, each element of list has 2 characters.
        #The first character represents the color of the pieces 'b' or 'w'
        #The second character represents the type of the piece, 'K', 'Q', 'R', 'N', 'B' or 'P'
        # "--" represents an empty space with no piece.
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--" ,"--", "--", "--", "--", "--", "--", "--"],
            ["--" ,"--", "--", "--", "--", "--", "--", "--"],
            ["--" ,"--", "--", "--", "--", "--", "--", "--"],
            ["--" ,"--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.whiteToMove = True
        self.movelog = []