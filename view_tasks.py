import json
from datetime import datetime
import os

# File to store tasks
TASKS_FILE = 'tasks.json'

# Priority mapping
PRIORITIES = {'high': 3, 'medium': 2, 'low': 1}

# Load tasks from file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# Add a task
def add_task(tasks, title, priority, due_date):
    tasks.append({
        'title': title,
        'priority': priority,
        'due_date': due_date,
        'completed': False
    })
    save_tasks(tasks)

# Remove a task
def remove_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
    else:
        print("Invalid task index.")

# Mark a task as completed
def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
        save_tasks(tasks)
    else:
        print("Invalid task index.")

# Display tasks
def display_tasks(tasks):
    for i, task in enumerate(tasks):
        status = "Done" if task['completed'] else "Not Done"
        print(f"{i}. {task['title']} [Priority: {task['priority'].capitalize()}] [Due: {task['due_date']}] [{status}]")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Complete task")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            title = input("Task title: ").strip()
            priority = input("Task priority (high, medium, low): ").strip().lower()
            if priority not in PRIORITIES:
                print("Invalid priority.")
                continue
            due_date = input("Due date (YYYY-MM-DD): ").strip()
            try:
                datetime.strptime(due_date, '%Y-%m-%d')
            except ValueError:
                print("Invalid date format.")
                continue
            add_task(tasks, title, priority, due_date)
            print("Task added.")
        elif choice == '3':
            index = int(input("Task index to remove: ").strip())
            remove_task(tasks, index)
            print("Task removed.")
        elif choice == '4':
            index = int(input("Task index to complete: ").strip())
            complete_task(tasks, index)
            print("Task marked as completed.")
        elif choice == '5':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
