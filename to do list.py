import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        selected_task = task_list.curselection()[0]
        task_list.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def clear_tasks():
    task_list.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, font=("Helvetica", 16))
entry.pack(side=tk.LEFT)

add_button = tk.Button(frame, text="Add Task", font=("Helvetica", 12), command=add_task)
add_button.pack(side=tk.LEFT, padx=10)

remove_button = tk.Button(frame, text="Remove Task", font=("Helvetica", 12), command=remove_task)
remove_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(root, text="Clear All", font=("Helvetica", 12), command=clear_tasks)
clear_button.pack(pady=10)

task_list = tk.Listbox(root, selectmode=tk.SINGLE, font=("Helvetica", 14), selectbackground="yellow")
task_list.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
