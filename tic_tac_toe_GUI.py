import tkinter as tk
import random
from tic_tac_toe_AI import random_ai, inter_ai, hard_ai

root = tk.Tk()

btn_font = ("Arial", 20)
lbl_font = ("Arial", 35)
menu_font = ("Arial", 12)

symbols = ['x', 'o']  # two symbols in a list, easy to change and easy to ramdonly pick
player = random.choice(symbols)
player2 = symbols[1] if player == symbols[0] else symbols[0]

player_first = True # flags if the player moves first or second, default first

# flag for game mode, 0 = local, 1 = vs random ai, 2 = vs intermediate ai, 3 = vs hard ai
mode = 0 
# stores callbacks to the ai functions to avoid using if clauses
AI = {1:random_ai, 2:inter_ai, 3:hard_ai}

titles = {0:"", 1:"vs random bot\n", 2:"vs intermediate bot\n", 3:"vs hard bot\n"}

def new_game(change_char_to=-1, player_first=True):
################################
# clears the board, then randomize player
################################    
    global board, player, firts, second, titles, player2
    for row in range(3):
        for column in range(3):
            board[row][column]['text'] = " "
            board[row][column].configure(bg="#F0F0F0", relief = "raised")

    if change_char_to == -1:
        player = random.choice(symbols)
        player2 = symbols[1] if player == symbols[0] else symbols[0]
    else:
        first.set(change_char_to == 0)
        second.set(change_char_to == 1)
        player = symbols[change_char_to]
    
    if not player_first: pass

    text = titles[mode]
    turn_lbl.configure(text= text + "{} turn".format("Your" if mode > 0 else player+"'s"))


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
    if len([board[row][col]['text'] for row in range(3) for col in range(3) 
                       if board[row][col]['text'] ==" "]) == 0:
        return -1
    
    return False
    


def player_turn(row, column):
################################
# each click on the board triggers this
# current player takes the turn 
# if it's vs ai, since it's triggered on button press
# the ai will follow up on every valid button press
# in the case that player goes second, new_game should initiate the first ai move
################################    
    global board

    if board[row][column]['text'] != " ":  #space already taken
        return  # do nothing, add warning/error message 

    if check_winner() is False:     #make sure players can't take turn after game is ended
        take_turn(row, column, True)
        if mode > 0 and check_winner() is False:    #also make sure ai does not take a turn after game is ended
            ai_row, ai_col = AI[mode](board, player2, player)
            take_turn(ai_row, ai_col, False)


def take_turn(row, column, is_player):
    global board, player, turn_lbl, titles

    board[row][column]['text'] = player if is_player else player2
    board[row][column].configure(relief="sunken")

    text = titles[mode]
    turn_result = check_winner()
    if turn_result is True:     # game won
        if is_player and mode > 0:    # player won vs ai
            turn_lbl.configure(text=text+"You WIN!")
        elif is_player and mode == 0:    # local pvp
            turn_lbl.configure(text="{} wins!".format(player))
        elif not is_player:     # ai won
            turn_lbl.configure(text=text+"You LOST!")

    elif turn_result is False:  # game continues, other player's turn
        if is_player and mode == 0:   # local pvp
            player = symbols[1] if player == symbols[0] else symbols[0]
            turn_lbl.configure(text="{}'s turn".format(player))
        else:           # vs ai the text doesnt need to be changed
            return

    elif turn_result == -1:     # tie
        turn_lbl.configure(text=text+"Tie!")
        

def new_char():
################################
# pops up another window that asks to replace existing symbols with new ones
# the input must be separated by a comma, if not the same prompt will pop up again
# if any side of the comma is only whitespaces or "" the corresponding symbol will not change
################################

    top = tk.Toplevel()
    top.title("top")
    top.geometry("400x200")
    y = root.winfo_screenheight()
    x = root.winfo_screenwidth()
    top.geometry("+{}+{}".format(x//2-200, y//2-50))


    def cleanup():
        global symbols
        new_chars = ent.get().strip(" ")
        try:
            comma = new_chars.index(",")
            symbols[0]  = new_chars[:comma] if new_chars else symbols[0]
            symbols[1] = new_chars[comma+1:] if new_chars[comma+1:] else symbols[1]

            new_game()
            top.destroy()
        except:
            top.destroy()
            new_char()
        

    top.rowconfigure([0,1,2], weight=1)
    top.columnconfigure([0,1], weight=1)
    txt = tk.Label(top, text="input characters,\n separated by comma:", font=("", 24))
    txt.grid(row=0, columnspan=2)
    ent = tk.Entry(top, width=20, font=("", 24))
    ent.grid(row=1, columnspan=2)
    ext_btn = tk.Button(top, text="confirm", command=cleanup, font=("", 18))
    cancel_btn = tk.Button(top, text="cancel",command=top.destroy, font=("", 18))
    ext_btn.grid(row=2, column=0, padx=1)
    cancel_btn.grid(row=2,column=1, padx=1)


def change_char(pos):
##############################################
# changes the player's current character
# and starts a new game
##############################################
    global player
    first.set(pos==0)
    second.set(pos==1)
    player = symbols[pos]
    new_game(pos)


def set_up_main_menu():
################################
# set up the menubar,
# contains: 
#          -change symbols
#          -start a new game
#          - to do: change to vs AI/local player
#              -switch difficulties of the AI
#              - difficulties are: random, intermediate and hard
################################
    global first, second
    menubar = tk.Menu(root)

    option_menu = tk.Menu(menubar, tearoff=0)
    option_menu.add_command(label="New Game", command=new_game)
    option_menu.add_command(label="New Characters", command=new_char)

    char_select_menu = tk.Menu(option_menu, tearoff=0)
    first = tk.BooleanVar()
    second = tk.BooleanVar()

    char_select_menu.add_checkbutton(label=symbols[0], onvalue=1, offvalue=0, 
                                     variable=first,command=lambda: change_char(0))
    char_select_menu.add_checkbutton(label=symbols[1], onvalue=1, offvalue=0, 
                                     variable=second,command=lambda: change_char(1))
    
    option_menu.add_cascade(label="Change character", menu=char_select_menu)
    option_menu.add_command(label="Quit", command=root.destroy)

    # to do: add player_order sub-menu, change checkbuttons to radio buttons^

    menubar.add_cascade(label="Options", menu=option_menu)

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
    mode_menu = tk.Menu(menubar, tearoff=0)
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

    set_up_screen()

    set_up_main_menu()
    new_game()
    root.mainloop()

if __name__ == '__main__':
    main()