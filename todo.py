import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime
import os

# File to store tasks
TASKS_FILE = 'tasks.json'

PRIORITIES = {'high': 3, 'edium': 2, 'low': 1}

def load_tasks() -> list:
    """Load tasks from file"""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

# Save all tasks to file
def save_tasks(tasks: list) -> None:
    """Save tasks to file"""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# Adding a task
def add_task(title: str, priority: str, due_date: str) -> None:
    """Add a task"""
    if not title or not due_date:
        messagebox.showerror("Error", "Please enter a title and due date.")
        return
    if priority not in PRIORITIES:
        messagebox.showerror("Error", "Invalid priority.")
        return
    try:
        datetime.strptime(due_date, '%Y-%m-%d')
    except ValueError:
        messagebox.showerror("Error", "Invalid date format.")
        return
    tasks.append({
        'title': title,
        'priority': priority,
        'due_date': due_date,
        'completed': False
    })
    save_tasks(tasks)
    messagebox.showinfo("Success", "Task added.")

# this function Remove or complete a task
def update_task(index: int, completed: bool = False) -> None:
    """Remove or complete a task"""
    if 0 <= index < len(tasks):
        if completed:
            tasks[index]['completed'] = True
        else:
            tasks.pop(index)
        save_tasks(tasks)
        messagebox.showinfo("Success", "Task updated.")
    else:
        messagebox.showerror("Error", "Invalid task index.")

# this function Displaying all the tasks
def display_tasks() -> None:
    """Display tasks"""
    task_list.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = "Done" if task['completed'] else "Not Done"
        task_list.insert(tk.END, f"{i}. {task['title']} [Priority: {task['priority'].capitalize()}] [Due: {task['due_date']}] [{status}]")

# now Creating main window
root = tk.Tk()
root.title("To-Do List Application")

# then Creating task list
task_list = tk.Listbox(root, width=50)
task_list.pack(padx=10, pady=10)

# Creating add task frame
add_task_frame = tk.Frame(root)
add_task_frame.pack(padx=10, pady=10)

tk.Label(add_task_frame, text="Title:").pack(side=tk.LEFT)
title_entry = tk.Entry(add_task_frame, width=20)
title_entry.pack(side=tk.LEFT)

tk.Label(add_task_frame, text="Priority:").pack(side=tk.LEFT)
priority_entry = tk.Entry(add_task_frame, width=10)
priority_entry.pack(side=tk.LEFT)

tk.Label(add_task_frame, text="Due Date:").pack(side=tk.LEFT)
due_date_entry = tk.Entry(add_task_frame, width=10)
due_date_entry.pack(side=tk.LEFT)

add_button = tk.Button(add_task_frame, text="Add Task", command=lambda: add_task(title_entry.get(), priority_entry.get(), due_date_entry.get()))
add_button.pack(side=tk.LEFT)

# here Creating remove task frame
remove_task_frame = tk.Frame(root)
remove_task_frame.pack(padx=10, pady=10)

tk.Label(remove_task_frame, text="Task Index:").pack(side=tk.LEFT)
index_entry = tk.Entry(remove_task_frame, width=5)
index_entry.pack(side=tk.LEFT)

remove_button = tk.Button(remove_task_frame, text="Remove Task", command=lambda: update_task(int(index_entry.get())))
remove_button.pack(side=tk.LEFT)

complete_button = tk.Button(remove_task_frame, text="Complete Task", command=lambda: update_task(int(index_entry.get()), completed=True))
complete_button.pack(side=tk.LEFT)

# here tasks will Loading
tasks = load_tasks()

# here tasks will Display
display_tasks()

# so that Start main loop and in which execute all features
root.mainloop()
