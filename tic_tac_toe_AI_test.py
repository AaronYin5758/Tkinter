import tkinter as tk
import random
import unittest
from tic_tac_toe_AI import *

def main():

    test_random()

    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()

    print("Running tests on intermediate ai:")
    inter_suite = unittest.TestSuite()
    inter_suite.addTests(loader.loadTestsFromTestCase(inter_test))
    runner.run(inter_suite)

    print("Running tests on hard ai:")
    hard_suite = unittest.TestSuite()
    hard_suite.addTests(loader.loadTestsFromTestCase(hard_test))
    runner.run(hard_suite)

def print_board(board):
    # for debugging purposes
    for i, tile in enumerate(board):
        if i in [2,5,8]:
            print(tile, end = '\n')
        else:
            print(tile, end = "|")
    
def buttonify(b:list[str]):
    # transforms a 1d list of chars into a 2d list of buttons to be used in ai file
    # this is for easier set up of test cases
    # also converts empty string("") into white space
    board = [[0,0,0], [0,0,0], [0,0,0]]
    for i, char in enumerate(b):
        char = char if char != "" else " "
        board[i//3][i%3] = tk.Button(text=str(char))
    return board
    
def test_random():
    # to test if the randomly generated position is valid
    # i.e. the returned index is an empty tile
    board = [0]*9
    for _ in range(10):
        for i in range(9):
            board[i] = "1" if random.choice([" ", "1", "-1"]) else " "
        board[2] = " "
        for _ in range(10):
            row, col = random_ai(buttonify(board), "1", "-1")
            #print(row, col)
            if board[row*3 + col] != " " or row == col == -1:
                print("error")
                print("row:", row, ", col:", col)
                print_board(board)
                return False
    print("random_ai passed", end="\n\n")

class inter_test(unittest.TestCase):
    # winning cases: both player wins, or either player wins on next move
    def test_self_win_over_player_win(self):
        # both players are one move away from winning
        board = buttonify(["1","1","", "2","2","", "","",""]) 
        self.assertEqual(inter_ai(board, "1", "2"), (0, 2)) 
        self.assertEqual(inter_ai(board, "2", "1"), (1, 2))

    def test_self_win(self):
        board = buttonify(["1","1"," ", "2"," "," ", " ","2"," "])
        self.assertEqual(inter_ai(board, "1", "2"), (0, 2))
    
    def test_player_win(self):
        board = buttonify(["1","1"," ", "2"," "," ", " ","2"," "])
        self.assertEqual(inter_ai(board, "2", "1"), (0, 2))

    # opening moves
    def test_first_move_on_empty_board(self):
        board = buttonify([""]*9)
        self.assertEqual(inter_ai(board, "1", "2"), (1,1))
    
    def test_second_move_when_center_free(self):
        board = buttonify(["","","", "2","","", "","",""])
        self.assertEqual(inter_ai(board, "1", "2"), (1,1))
    
    def test_first_move_when_center_taken(self):
        board = buttonify(["","","", "","2","", "","",""])
        self.assertIn(inter_ai(board, "1", "2"), [(0,0), (0,2), (2,0), (2,2)])

    # closing move
    def test_move_on_full_board(self):
        board = buttonify(["1","2","1", "1","2","1", "2","1","2"])
        self.assertEqual(inter_ai(board, "1", "2"), (-1,-1))
    
    def test_one_tile_left(self):
        board = buttonify(["1","2","1", "1","","1", "2","1","2"])
        self.assertEqual(inter_ai(board, "2", "1"), (1, 1))
    
    # normal moves
    def test_move_on_corner(self):
        board = buttonify(["","1","2", "","2","1", "1","","2"])
        self.assertEqual(inter_ai(board, "1", "2"), (0, 0))
    
    def test_move_no_corners(self):
        board = buttonify(["1","1","2", "","2","1", "2","","1"])
        self.assertIn(inter_ai(board, "1", "2"), [(1,0), (2,1)])
    
    def test_move_center_free(self):
        board = buttonify(["2","1","2", "","","2", "1","2","1"])
        self.assertEqual(inter_ai(board, "1", "2"), (1, 1))


class hard_test(unittest.TestCase):
    # prio self win
    def test_self_win(self):
        board = buttonify(["1","1","", "2","","", "2","",""])
        self.assertEqual(hard_ai(board, "1", "2"), (0, 2))
    
    def test_block_player_win(self):
        board = buttonify(["1","1","", "2","","", "2","",""])
        self.assertEqual(hard_ai(board, "2", "1"), (0, 2))

    def test_self_win_over_player(self):
        board = buttonify(["1","1","", "2","2","", "","",""]) 
        self.assertEqual(inter_ai(board, "1", "2"), (0, 2)) 
        self.assertEqual(inter_ai(board, "2", "1"), (1, 2))

    def test_move_on_empty_board(self):
        board = buttonify([""]*9)
        self.assertNotEqual(hard_ai(board, "1", "2"), (-1, -1))

    def test_move_on_full_board(self):
        board = buttonify([str(x%3) for x in range(9)])
        self.assertEqual(hard_ai(board, "1", "2"), (-1, -1))

if __name__ == '__main__':
    main()
    #unittest.main()