import tkinter as tk

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)


def clear():
    entry.delete(0, tk.END)


def calculate():
    try:
        result = eval(entry.get())  
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


root = tk.Tk()
root.title("Basic Calculator")


entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]


for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), command=calculate)
    else:
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)


clear_button = tk.Button(root, text="C", width=10, height=3, font=("Arial", 18), command=clear)
clear_button.grid(row=5, column=0, columnspan=4)


root.mainloop()
