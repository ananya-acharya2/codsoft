import json
import os

class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
       
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Error: Unable to load tasks due to file corruption. Starting fresh.")
                return []
        return []

    def save_tasks(self):
       
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        
        self.tasks.append({"task": task})
        self.save_tasks()
        print(f"Task '{task}' added successfully.")

    def update_task(self, task_number, new_task):
       
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["task"] = new_task
            self.save_tasks()
            print(f"Task {task_number} updated successfully.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f"Task '{removed_task['task']}' deleted successfully.")
        else:
            print("Invalid task number.")

    def show_tasks(self):
        
        if not self.tasks:
            print("No tasks found!")
        else:
            print("\nTo-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task['task']}")

    def clear_tasks(self):
        
        self.tasks = []
        self.save_tasks()
        print("All tasks cleared!")


def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. Show Tasks")
        print("5. Clear Tasks")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("!!!! Invalid input !!!!")
            continue

        if choice == 1:
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == 2:
            try:
                task_number = int(input("Enter task number to update: "))
                new_task = input("Enter the updated task: ")
                todo_list.update_task(task_number, new_task)
            except ValueError:
                print("Invalid task number. Please enter a valid number.")
        elif choice == 3:
            try:
                task_number = int(input("Enter task number to delete: "))
                todo_list.delete_task(task_number)
            except ValueError:
                print("Invalid task number. Please enter a valid number.")
        elif choice == 4:
            todo_list.show_tasks()
        elif choice == 5:
            confirm = input("Are you sure you want to clear all tasks? (y/n): ")
            if confirm.lower() == 'y':
                todo_list.clear_tasks()
        elif choice == 6:
            print("!!!Goodbye!!!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
