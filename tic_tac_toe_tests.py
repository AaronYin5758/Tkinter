import tkinter as tk
import random
from tic_tac_toe_AI import *

def main():

    test_random()

def print_board(board):
    # for debugging purposes
    for row in range(3):
        for col in range(3):
            if col == 2:
                print(board[row][col]['text'])
            else:
                print(board[row][col]['text'], end = ",")
    
def buttonify(b):
    # transforms a 1d list of chars into a 2d list of buttons to be used in ai file
    # this is for easier set up of test cases
    board = [[0,0,0], [0,0,0], [0,0,0]]
    for i, char in enumerate(b):
        board[i//3][i%3] = tk.Button(text=char)
    return board
    
def test_random():
    # to test if the randomly generated position is valid
    # i.e. the returned index is an empty tile
    board = [0]*9
    for _ in range(100):
        for i in range(9):
            board[i] = "1" if random.randint(0,1) else " "
        board[2] = " "
        for _ in range(100):
            row, col = random_ai(buttonify(board), "", "")
            #print(row, col)
            if board[row*3 + col] != " ":
                print("error")
                print("row:", row, ", col:", col)
                print_board(board)
                return False
    print("random_ai passed")

def test_inter():
    board = [0] * 9
    


if __name__ == '__main__':
    main()