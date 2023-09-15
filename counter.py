import tkinter as tk

def increase():
    val = int(lbl_counter["text"])
    lbl_counter["text"] = f"{val + 1}"

def decrease():
    val = int(lbl_counter["text"])
    lbl_counter["text"] = f"{val - 1}"


def set_up(root):
    root.title("Counter")
    root.eval("tk::PlaceWindow . center")

    root.rowconfigure(0, minsize=100, weight=1)
    root.columnconfigure([0,1,2], minsize=100, weight=1)

    btn_minus = tk.Button(master=root, text="-", font=("Arial", 20), relief="raised", command=decrease)
    btn_minus.grid(row=0, column=0, sticky="nsew")

    global lbl_counter
    lbl_counter = tk.Label(master=root, text="0", font=("Arial", 20), relief="sunken")
    lbl_counter.grid(row=0, column=1, sticky="nwse")

    btn_plus = tk.Button(master=root, text="+", font=("Arial", 20), relief="raised", command=increase)
    btn_plus.grid(row=0, column=2, sticky="snew")


def main():
    root = tk.Tk()
    set_up(root)


    root.mainloop()

if __name__ == "__main__":
    main()