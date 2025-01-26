import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = task_entry.get()
    if task.strip() != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Function to clear all tasks
def clear_tasks():
    task_listbox.delete(0, tk.END)

# Main application window
app = tk.Tk()
app.title("To-Do List")
app.geometry("400x400")

# Input field and buttons
task_entry = tk.Entry(app, width=35)
task_entry.pack(pady=10)

add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(app, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

clear_button = tk.Button(app, text="Clear Tasks", command=clear_tasks)
clear_button.pack(pady=5)

# Listbox to display tasks
task_listbox = tk.Listbox(app, width=50, height=15)
task_listbox.pack(pady=10)

# Run the application
app.mainloop()
