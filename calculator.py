# simple calculator GUI
# contains:
#       -a text field, could be label since it is only a simple calculator
#       -buttons :
#           -number pads from 0-9
#           -signs: +, -, x, /, (), =, C
# buttons are in a 4x5 grid
#################################
# roughly looks like this
#   -------------------------
#   |             9+10x(3-2)|     
#   -------------------------
#   |  1  |  2  |  3  |  +  |
#   |  4  |  5  |  6  |  -  | 
#   |  7  |  8  |  9  |  x  |
#   |  (  |  0  |  )  |  /  |
#   |     C     |     =     |
#   -------------------------
##################################

import tkinter as tk

fonts = ("Arial", 18)  #font of all the buttons
text = ""

def add_to_text(char):
    # adds whatever char to the end of the text 
    # then update text field
    global text
    text+= str(char)
    text_field.config(text=text)

def evaluate_text():
    # evaluates whatever is in the text field, 
    # then updates the text field
    global text
    try:
        text = str(eval(text))
        text_field.config(text=text)
    except:
        text_field.config(text="ERROR")

def clear_text():
    #clears the text field
    global text
    text = ""
    text_field.config(text=text)

#set up the window
root = tk.Tk()
root.eval("tk::PlaceWindow . center")
root.title("Calculator")
root.geometry("400x350")
root.rowconfigure([0,1,2,3,4,5,6], weight=1)
root.columnconfigure([0,1,2,3], weight=1)

text_field = tk.Label(master=root, height=2, text="0", font=("Arial", 30))
text_field.grid(row=0, columnspan=4, sticky="e")


#set up all the number buttons, since they are basically copy paste
#use lambda functions to save wrting extra functions 
btn_num1 = tk.Button(master=root, command= lambda: add_to_text(1), text="1", font=fonts)
btn_num2 = tk.Button(master=root, command= lambda: add_to_text(2), text="2", font=fonts)
btn_num3 = tk.Button(master=root, command= lambda: add_to_text(3), text="3", font=fonts)
btn_num4 = tk.Button(master=root, command= lambda: add_to_text(4), text="4", font=fonts)
btn_num5 = tk.Button(master=root, command= lambda: add_to_text(5), text="5", font=fonts)
btn_num6 = tk.Button(master=root, command= lambda: add_to_text(6), text="6", font=fonts)
btn_num7 = tk.Button(master=root, command= lambda: add_to_text(7), text="7", font=fonts)
btn_num8 = tk.Button(master=root, command= lambda: add_to_text(8), text="8", font=fonts)
btn_num9 = tk.Button(master=root, command= lambda: add_to_text(9), text="9", font=fonts)
btn_num0 = tk.Button(master=root, command= lambda: add_to_text(0), text="0", font=fonts)

#set up the symbol buttons
btn_add = tk.Button(master=root, text="+", font=fonts, command= lambda: add_to_text("+"))
btn_subtract = tk.Button(master=root, text="-", font=fonts, command= lambda: add_to_text("-"))
btn_multiply = tk.Button(master=root, text="*", font=fonts, command= lambda: add_to_text("*"))
btn_divide = tk.Button(master=root, text="/", font=fonts, command= lambda: add_to_text("/"))
btn_left_bracket = tk.Button(master=root, text="(", font=fonts, command= lambda: add_to_text("("))
btn_right_bracket = tk.Button(master=root, text=")", font=fonts, command= lambda: add_to_text(")"))
btn_clear = tk.Button(master=root, text="C", font=fonts, command=clear_text)
btn_equal = tk.Button(master=root, text="=", font=fonts, command=evaluate_text)

#place the buttons onto the window
btn_num1.grid(row=1, column=0, sticky="nsew")
btn_num2.grid(row=1, column=1, sticky="nsew")
btn_num3.grid(row=1, column=2, sticky="nsew")
btn_num4.grid(row=2, column=0, sticky="nsew")
btn_num5.grid(row=2, column=1, sticky="nsew")
btn_num6.grid(row=2, column=2, sticky="nsew")
btn_num7.grid(row=3, column=0, sticky="nsew")
btn_num8.grid(row=3, column=1, sticky="nsew")
btn_num9.grid(row=3, column=2, sticky="nsew")
btn_num0.grid(row=4, column=1, sticky="nsew")

btn_add.grid(row=1, column=3, sticky="nsew")
btn_subtract.grid(row=2, column=3, sticky="nsew")
btn_multiply.grid(row=3, column=3, sticky="nsew")
btn_divide.grid(row=4, column=3, sticky="nsew")
btn_left_bracket.grid(row=4, column=0, sticky="nsew")
btn_right_bracket.grid(row=4, column=2, sticky="nsew")
btn_clear.grid(row=5, column=0, columnspan=2, sticky="nsew")
btn_equal.grid(row=5, column=2, columnspan=2, sticky="nsew")

root.mainloop()

