import tkinter as tk

class My_gui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("MessageBox")

        # self.label1 = tk.Label(self.root, text='Hi!', font=('Arial', 20), fg="white", bg="black", height=5, width=5)
        # self.label1.pack() 

        # self.test_btn = tk.Button(self.root, text="test button", height=5, width=10)
        # self.test_btn.pack()

        self.test_textbox = tk.Text(self.root, height=5, font=("Arial", 20))
        self.test_textbox.pack()

        self.checkVal = tk.IntVar()
        self.checkbox = tk.Checkbutton(self.root, text="Show Messagebox", font=("Arial", 20), variable=self.checkVal)
        self.checkbox.pack()

        self.messageBtn = tk.Button(self.root, text="Show Message", command=self.message, font=("Arial", 20))
        self.messageBtn.pack()

        self.root.mainloop()
    
    def message(self):
        if self.checkVal.get() == 1:
            print(self.test_textbox.get("1.0", tk.END))
        else:
            print("Message")

My_gui()
