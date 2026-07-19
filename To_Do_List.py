import json
import os

# Filename to store tasks
DATA_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    if not tasks:
        print("\nYour task list is empty.")
    else:
        print("\n--- Your Tasks ---")
        for idx, task in enumerate(tasks, 1):
            status = "[Done]" if task['completed'] else "[Pending]"
            print(f"{idx}. {status} {task['name']}")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task | 2. View Tasks | 3. Mark Completed | 4. Delete Task | 5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter task name: ")
            tasks.append({"name": name, "completed": False})
            save_tasks(tasks)
            print("Task added.")
            
        elif choice == '2':
            display_tasks(tasks)
            
        elif choice == '3':
            display_tasks(tasks)
            idx = int(input("Enter task number to mark as completed: ")) - 1
            if 0 <= idx < len(tasks):
                tasks[idx]['completed'] = True
                save_tasks(tasks)
                print("Task marked as completed.")
                
        elif choice == '4':
            display_tasks(tasks)
            idx = int(input("Enter task number to delete: ")) - 1
            if 0 <= idx < len(tasks):
                removed = tasks.pop(idx)
                save_tasks(tasks)
                print(f"Deleted: {removed['name']}")
                
        elif choice == '5':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()