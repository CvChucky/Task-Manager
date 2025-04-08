# To-Do List App

tasks = []  # This is where we'll store tasks

def show_menu():
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")

def add_task():
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def view_tasks():
    if tasks:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("No tasks to show.")

def delete_task():
    view_tasks()
    if tasks:
        try:
            task_number = int(input("Enter the task number you want to delete: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' deleted!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1/2/3/4): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the app
main()
