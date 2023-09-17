import tkinter as tk
import random

btn_font = ("Arial", 20)
lbl_font = ("Arial", 35)
menu_font = ("Arial", 12)

symbols = ['x', 'o']  # two symbols in a list, easy to change and easy to ramdonly pick
player = random.choice(symbols)
  
# flag for game mode, 0 = local 2 player, 1 = vs random ai, 2 = vs intermediate ai, 3 = vs hard ai
mode = 0 

def new_game():
################################
# clears the board, then randomize player
################################    
    global board, player
    for row in range(3):
        for column in range(3):
            board[row][column]['text'] = " "
            board[row][column].configure(bg="#F0F0F0")

    player = random.choice(symbols)
    titles = {0:"", 1:"vs random bot\n", 2:"vs intermediate bot\n", 3:"vs hard bot\n"}
    text = titles[mode]
    turn_lbl.configure(text= text + player + "'s turn")


def check_winner():
################################
# check if there is a winner/full board
# highlights the winning row/column/diagonal
# returns True if there is a winner
#         False if there is no winner
#         -1 is the board is full
################################    
    global board
   
    for row in range(3):
        if board[row][0]['text'] == board[row][1]['text'] == board[row][2]['text'] != " ": # check rows
            board[row][0].configure(bg="green")
            board[row][1].configure(bg="green")
            board[row][2].configure(bg="green")
            return True

        if board[0][row]['text'] == board[1][row]['text'] == board[2][row]['text'] != " ": #check columns
            board[0][row].configure(bg="green")
            board[1][row].configure(bg="green")
            board[2][row].configure(bg="green")
            return True
        
    if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != " ": #check diagonal
        board[0][0].configure(bg="green")
        board[1][1].configure(bg="green")
        board[2][2].configure(bg="green")
        return True
    
    if board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != " ": #check diagonal
        board[0][2].configure(bg="green")
        board[1][1].configure(bg="green")
        board[2][0].configure(bg="green")
        return True

    space = 0     
    for row in range(3):
        for column in range(3):
            if board[row][column]['text'] != " ":
                space += 1
    if space == 9:
        return -1
    
    return False
    


def player_turn(row, column):
################################
# each click on the board triggers this
# current player takes the turn 
################################    
    global board

    if board[row][column]['text'] != " ":  #space already taken
        return  # do nothing, add warning/error message 

    if check_winner() is False:     #make sure players can't take turn after game is ended
            take_turn(row, column)


def take_turn(row, column):
    global board, player, turn_lbl

    board[row][column]['text'] = player
    board[row][column].configure(relief="sunken")
    turn_result = check_winner()
    if turn_result is True:     # game won
        turn_lbl.configure(text="{} wins!".format(player), font=lbl_font)
    elif turn_result is False:  # game continues, other player's turn
        player = symbols[1] if player == symbols[0] else symbols[0]
        turn_lbl.configure(text="{}'s turn".format(player), font=lbl_font)
    elif turn_result == -1:     # tie
        turn_lbl.configure(text="Tie!", font=lbl_font)
        

def change_char():
################################
# pops up another window that asks to replace existing symbols with new ones
# 
################################

    top = tk.Toplevel()
    top.title("top")
    top.geometry("400x200")
    y = root.winfo_screenheight()
    x = root.winfo_screenwidth()
    top.geometry("+{}+{}".format(x//2-200, y//2-50))


    def cleanup():
        global symbols
        symbols[0], symbols[1] = ent.get().strip("").split(",")
        new_game()
        top.destroy()

    top.rowconfigure([0,1,2], weight=1)
    top.columnconfigure([0,1], weight=1)
    txt = tk.Label(top, text="input characters\n separated by comma:", font=("", 24))
    txt.grid(row=0, columnspan=2)
    ent = tk.Entry(top, width=20, font=("", 24))
    ent.grid(row=1, columnspan=2)
    ext_btn = tk.Button(top, text="confirm", command=cleanup, font=("", 18))
    cancel_btn = tk.Button(top, text="cancel",command=top.destroy, font=("", 18))
    ext_btn.grid(row=2, column=0, padx=1)
    cancel_btn.grid(row=2,column=1, padx=1)


def set_up_menu():
################################
# set up the menubar,
# contains: 
#          -change symbols
#          -start a new game
#          - to do: change to vs AI/local player
#              -switch difficulties of the AI
#              - difficulties are: random, intermediate and hard
################################
    menubar = tk.Menu(root)

    option_menu = tk.Menu(menubar, tearoff=0)
    option_menu.add_command(label="Change Characters", command=change_char)
    option_menu.add_command(label="New Game", command=new_game)
    option_menu.add_command(label="Quit", command=root.destroy)

    menubar.add_cascade(label="Options", menu=option_menu)

    mode_menu = tk.Menu(menubar, tearoff=0)
    # private functions to change the mode variable to avoid using lambda
    def local_mode():
        global mode
        mode = 0
        new_game()
    def random_mode():
        global mode
        mode = 1
        new_game()
    def inter_mode():
        global mode
        mode = 2
        new_game()
    def hard_mode():
        global mode
        mode = 3
        new_game()
    mode_menu.add_command(label="vs local player", command = local_mode)
    ai_menu = tk.Menu(menubar, tearoff = 0)
    ai_menu.add_command(label="vs random bot", command=random_mode)
    ai_menu.add_command(label="vs intermediate bot", command=inter_mode)
    ai_menu.add_command(label="vs hard bot", command=hard_mode)

    menubar.add_cascade(label="Modes", menu=mode_menu)
    mode_menu.add_cascade(label="vs AI", menu=ai_menu)

    root.config(menu=menubar)


def set_up_screen():
################################
# set up the grid layout and board
# 
################################    
    global turn_lbl, board

    root.title("Tic-Tac-Toe")
    #set up window size
    window_width, window_height = 400, 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    #make sure window is always in the center, might not work with duel screen set up
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    root.rowconfigure([0,2], weight=1)
    root.rowconfigure([1], weight=0)
    root.columnconfigure(0, weight=1)

    turn_lbl = tk.Label(root, text=player + "'s turn", font=lbl_font)
    turn_lbl.grid(row=0, column = 0, sticky="Nwes")


    board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

    buttons_frm = tk.Frame(root)
    buttons_frm.columnconfigure([0,1,2], weight=1)
    buttons_frm.rowconfigure([0,1,2], weight=1)
    # button frame slightly padded so that there is more contrast between solid and sunken states
    buttons_frm.grid(row=2, column=0, sticky="nsew", pady=(0,1), padx=1)

    for row in range(3):
        for column in range(3):
            board[row][column] = tk.Button(buttons_frm, font=btn_font, text=" ", width=5, height=2,
                                           relief="solid",
                                       command=lambda row=row, column=column: player_turn(row, column))
            board[row][column].grid(row=row, column=column, sticky="nsew")

def main():
    global root
    root = tk.Tk()
    
    set_up_screen()

    set_up_menu()

    root.mainloop()

if __name__ == '__main__':
    main()