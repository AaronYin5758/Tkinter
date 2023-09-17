# This file is for the different levels of AI for the game tic-tac-toe
# 3 main levels are: random, intermediate, hard
# all 3 fill follow the pattern of:
#                               - input: board, a 3x3 matrix, and the symbols of ai and player
#                               - output: the index where the AI will make its move
import tkinter as tk
import random


def isWinner(board, symbol):
    return (board[0] == symbol and board[1] == symbol and board[2] == symbol or 
            board[3] == symbol and board[4] == symbol and board[5] == symbol or 
            board[6] == symbol and board[7] == symbol and board[8] == symbol or #3 rows checked
            board[0] == symbol and board[3] == symbol and board[6] == symbol or 
            board[1] == symbol and board[4] == symbol and board[7] == symbol or 
            board[2] == symbol and board[5] == symbol and board[8] == symbol or #3 columns checked
            board[0] == symbol and board[4] == symbol and board[8] == symbol or 
            board[2] == symbol and board[4] == symbol and board[6] == symbol) #2 crosses checked

def parse_board(board):
    # transform the 2d list of buttons to a 1d list of chars
    b, empty = [], []
    for row in range(3):
        for col in range(3):
            b.append(board[row][col]['text'])
            if b[-1] == " ":
                empty.append(len(b)-1)
    return (b, empty)

def index_to_2d(i):
    # convert 1d index from 0-8 to 2d index (row, col), row, col in [0, 3]
    return (i//3, 1%3)

def random_ai(board, symbol, player):
    #chooses an available tile randomly
    return random.choice(parse_board(board)[1])

def inter_ai(board, symbol, player):
    # ai looks at state of board, then decides its move greedily based on the following
    # priorities:
    #           1.winning 
    #           2.prevent player from winning 
    #           3.choose the center, a corner, or a mid tile (the tile with most "empty" directions)
    ###############################################################
    b, empty = parse_board(board)

    if len(empty) == 9:   # all tiles free
        return index_to_2d(4)
    elif len(empty) == 8:  # all but one tile free
        if b[4] == " ": return index_to_2d(4)
        else: return index_to_2d(random.choice([0,2,6,8]))
    elif len(empty) == 1:   # only one tile free
        return index_to_2d(empty[0])

    for ind in empty:
        temp_b = b[:]
        temp_b[ind] = symbol
        if isWinner(temp_b, symbol):
            return index_to_2d(ind)
        temp_b[ind] = player
        if isWinner(temp_b, player):
            return index_to_2d(ind)
    

        