# This file is for the different levels of AI for the game tic-tac-toe
# 3 main levels are: random, intermediate, hard
# all 3 fill follow the pattern of:
#                               - input: board, a 3x3 matrix, and the symbols of ai and player
#                               - output: the index where the AI will make its move
import tkinter as tk
import random
from math import inf

def check_winner(board:list[str]) -> (bool, str):
    # checks the board and returns True and the winning side or False and None
    if board[0] == board[1] == board[2]:  #check 3 rows
        return True, board[0]
    elif board[3] == board[4] == board[5]:
        return True, board[3]
    elif board[6] == board[7] == board[8]:
        return True, board[6]
    elif board[0] == board[3] == board[6]:  #check 3 columns
        return True, board[0]
    elif board[1] == board[4] == board[7]:
        return True, board[1]
    elif board[2] == board[5] == board[8]:
        return True, board[2]
    elif board[0] == board[4] == board[8]:  #check 2 diagonals
        return True, board[0]
    elif board[2] == board[4] == board[6]:
        return True, board[2]
    empty = board.count(" ")
    if empty > 0:
        return False, None 
    else:
        return False, "DRAW"

def parse_board(board:list[list[tk.Button]], symbol:str, player:str)->(list[int], list[int]):
    # transform the 2d list of buttons to a 1d list of chars
    # also changes both players' symbols to 1 and -1 respectively, this makes implementing hard ai easier
    # the indexes are [0, 8] for consistency
    b, empty = [], []
    for row in range(3):
        for col in range(3):
            if board[row][col]['text'] == symbol:
                b.append("1")
            elif board[row][col]['text'] == player:
                b.append("-1")
            else:
                b.append(" ")
                empty.append(len(b)-1)
    #1print("Parse:", b, empty)
    return (b, empty)

def index_to_2d(i):
    # convert 1d index from 0-8 to 2d index (row, col), row, col in [0, 3]
    return (i//3, i%3)

def random_ai(board, symbol, player)->(int, int):
    #chooses an available tile randomly
    _, empty = parse_board(board, symbol, player)
    return index_to_2d(random.choice(empty)) if empty else (-1,-1)

def inter_ai(board, symbol, player):
    # ai looks at state of board, then decides its move greedily based on the following
    # priorities:
    #           1.winning 
    #           2.prevent player from winning 
    #           3.choose the center, a corner, or a middles tile (the tile with most "empty" directions)
    ###############################################################
    b, empty = parse_board(board, symbol, player)

    if not empty: # full board, something wrong
        return -1
    elif len(empty) == 9:   # all tiles free
        return index_to_2d(4)
    elif len(empty) == 8:  # all but one tile free
        if b[4] == " ": return index_to_2d(4)
        else: return index_to_2d(random.choice([0,2,6,8]))
    elif len(empty) == 1:   # only one tile free
        return index_to_2d(empty[0])


    # loop through every empty tile and find the winning play of both players
    self_win, player_win = None, None
    for ind in empty:    
        temp_b = b[:]
        temp_b[ind] = "1"
        game_won, winner = check_winner(temp_b)
        if game_won and winner == "1":
            self_win = ind
        temp_b[ind] = "-1"
        game_won, winner = check_winner(temp_b)
        if game_won and winner == "-1":
            player_win = ind
    
    # prioritize self win over player win
    if self_win: return index_to_2d(self_win)   
    if player_win: return index_to_2d(player_win)

    # prioritize center, then corners, then middles
    empty_corners, empty_mids = [x for x in [0,2,6,8] if x in empty], [x for x in [1,3,5,7] if x in empty]
    if b[4] == " ": return index_to_2d(4)
    elif empty_corners: return index_to_2d(random.choice(empty_corners))
    else:   return index_to_2d(random.choice(empty_mids))


def hard_ai(board, symbol, player):
    # use alpha beta pruning to determine which tile to pick
    b, empty = parse_board(board)
    res = alpha_beta(b, empty, inf, -inf, "1")
    return res[0]

def alpha_beta(board, empty, alpha, beta, cur_symbol):
    # returns position, score
    # "1" is ai/self, "-1" is player thus self winning scores positive, and tie score neutral
    # alpha/beta are the upper/lower limits
    # cur_symbol measures the current states, whether it's alpha or beta
    game_won, winner = check_winner(board)
    pos = -1
    if len(empty) == 0 or winner:
        score = 0
        if winner == "1": score = 1
        elif winner == "-1": score = -1
        return [pos, score]
    
    for tile in empty:
        board[tile] = cur_symbol
        temp_e = empty[:]
        temp_e.remove(tile)
        res, score = alpha_beta(board, temp_e, alpha, beta, str(-int(cur_symbol)))
        if cur_symbol == "1":
            # max node
            if score > alpha: # update alpha
                alpha, pos = score, res
        else:
            if score < beta:
                beta, pos = score, res

        board[tile] = " "  # reset(backtrack)

        if alpha >= beta:  # cut off branch
            break

    if cur_symbol == "1":
        return pos, alpha
    else:
        return pos, beta