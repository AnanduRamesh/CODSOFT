import sys

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'status': 'Pending'})
        print(f"Task '{task}' added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
            return
        print("\nYour To-Do List:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task['task']} - {task['status']}")

    def update_task(self, task_number, new_task):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]['task'] = new_task
            print(f"Task {task_number} updated successfully.")
        else:
            print("Invalid task number.")

    def update_status(self, task_number, status):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]['status'] = status
            print(f"Status of task {task_number} updated to {status}.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' deleted successfully.")
        else:
            print("Invalid task number.")

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Update a task")
    print("4. Update task status")
    print("5. Delete a task")
    print("6. Exit")

def main():
    todo_list = ToDoList()

    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks()
            task_number = int(input("Enter the task number to update: "))
            new_task = input("Enter the new task description: ")
            todo_list.update_task(task_number, new_task)
        elif choice == '4':
            todo_list.view_tasks()
            task_number = int(input("Enter the task number to update status: "))
            status = input("Enter the new status (Pending/In Progress/Completed): ")
            todo_list.update_status(task_number, status)
        elif choice == '5':
            todo_list.view_tasks()
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == '6':
            print("Exiting the To-Do List application.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
