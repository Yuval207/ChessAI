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
    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = '--'
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.movelog.append(move) #log the move so we can undo it later
        self.whiteToMove = not self.whiteToMove #swap Players

    
    #Undo Last move made

    def undoMove(self):
        if len(self.movelog) != 0:
            move = self.movelog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove 


class Move:
    # maps keys to values
    # key : value
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4, 
                   "5": 3, "6": 2, "7": 1, "8":0}
    
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3, 
                   "e": 4, "f": 5, "g": 6, "h":7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]



    def getChessNotation(self):
        # add this to make real chess notation
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)
    

    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]