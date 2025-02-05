import sys
import json
import os
from datetime import datetime

# File to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from the JSON file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

# Save tasks to the JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Generate a unique ID for a new task
def generate_id(tasks):
    return max([task['id'] for task in tasks], default=0) + 1

# Add a new task
def add_task(description):
    tasks = load_tasks()
    new_task = {
        "id": generate_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")

# Update an existing task
def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully")
            return
    print(f"Error: Task with ID {task_id} not found")

# Delete a task
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    if len(tasks) == len(load_tasks()):
        print(f"Error: Task with ID {task_id} not found")
    else:
        save_tasks(tasks)
        print(f"Task {task_id} deleted successfully")

# Mark a task as in-progress
def mark_in_progress(task_id):
    update_task_status(task_id, "in-progress")

# Mark a task as done
def mark_done(task_id):
    update_task_status(task_id, "done")

# Helper function to update task status
def update_task_status(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as {status}")
            return
    print(f"Error: Task with ID {task_id} not found")

# List tasks based on status or all tasks
def list_tasks(status=None):
    tasks = load_tasks()
    filtered_tasks = tasks if status is None else [task for task in tasks if task['status'] == status]
    if not filtered_tasks:
        print("No tasks found")
        return
    for task in filtered_tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['createdAt']}, Updated At: {task['updatedAt']}")

# Main function to handle CLI commands
def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [arguments]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Missing task description")
            sys.exit(1)
        add_task(sys.argv[2])

    elif command == "update":
        if len(sys.argv) < 4:
            print("Error: Missing task ID or new description")
            sys.exit(1)
        try:
            task_id = int(sys.argv[2])
            new_description = sys.argv[3]
            update_task(task_id, new_description)
        except ValueError:
            print("Error: Task ID must be an integer")
            sys.exit(1)

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: Missing task ID")
            sys.exit(1)
        try:
            task_id = int(sys.argv[2])
            delete_task(task_id)
        except ValueError:
            print("Error: Task ID must be an integer")
            sys.exit(1)

    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Error: Missing task ID")
            sys.exit(1)
        try:
            task_id = int(sys.argv[2])
            mark_in_progress(task_id)
        except ValueError:
            print("Error: Task ID must be an integer")
            sys.exit(1)

    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Error: Missing task ID")
            sys.exit(1)
        try:
            task_id = int(sys.argv[2])
            mark_done(task_id)
        except ValueError:
            print("Error: Task ID must be an integer")
            sys.exit(1)

    elif command == "list":
        status = None
        if len(sys.argv) > 2:
            status_arg = sys.argv[2].lower()
            if status_arg in ["todo", "in-progress", "done"]:
                status = status_arg
            else:
                print("Error: Invalid status. Use 'todo', 'in-progress', or 'done'")
                sys.exit(1)
        list_tasks(status)

    else:
        print("Error: Invalid command")
        sys.exit(1)

if __name__ == "__main__":
    main()