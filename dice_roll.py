import tkinter as tk

class Dice_Roll_GUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.rowconfigure([0,1], minsize=300, weight=1)
        self.root.columnconfigure(0, minsize=300, weight=1)

        self.rollBtn = tk.Button(self.root, text="Roll", font=("Arial", 20), command=self.roll, relief="raised")
        self.rollBtn.grid( row=0, sticky="nswe")

        #lbl can be empty, i.e. without text
        self.result_lbl = tk.Label(self.root, text="ROLL ME!", font=("Arial", 20))
        self.result_lbl.grid( row=1, sticky="nswe")

        self.root.mainloop()

    def roll(self):
        #uses random to roll a six-sided dice with different colours on each side 
        import random
        colours = ["red", "orange", "yellow", "green", "blue", "purple"]
        val = random.randrange(1,7)
        self.result_lbl["text"] = str(val)
        self.result_lbl["background"] = colours[val-1]

Dice_Roll_GUI()