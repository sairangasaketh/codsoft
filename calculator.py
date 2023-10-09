import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def add():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def subtract():
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def multiply():
    first_number = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def divide():
    first_number = entry.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def equal():
    second_number = entry.get()
    entry.delete(0, tk.END)
    if math == "addition":
        entry.insert(0, f_num + float(second_number))
    elif math == "subtraction":
        entry.insert(0, f_num - float(second_number))
    elif math == "multiplication":
        entry.insert(0, f_num * float(second_number))
    elif math == "division":
        if float(second_number) == 0:
            entry.insert(0, "Error")
        else:
            entry.insert(0, f_num / float(second_number))

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry field
entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Define buttons
button_1 = tk.Button(root, text="1", padx=20, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=20, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=20, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=20, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=20, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=20, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=20, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=20, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=20, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=20, pady=20, command=lambda: button_click(0))
button_add = tk.Button(root, text="+", padx=20, pady=20, command=add)
button_subtract = tk.Button(root, text="-", padx=20, pady=20, command=subtract)
button_multiply = tk.Button(root, text="*", padx=20, pady=20, command=multiply)
button_divide = tk.Button(root, text="/", padx=20, pady=20, command=divide)
button_equal = tk.Button(root, text="=", padx=20, pady=20, command=equal)
button_clear = tk.Button(root, text="C", padx=20, pady=20, command=clear)

# Add buttons to the grid
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_subtract.grid(row=4, column=2)
button_multiply.grid(row=5, column=0)
button_divide.grid(row=5, column=1)
button_equal.grid(row=5, column=2)
button_clear.grid(row=4, column=3)

root.mainloop()
