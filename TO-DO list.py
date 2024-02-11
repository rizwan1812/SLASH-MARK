def add_task(tasks, task):
    tasks.append(task)
    print("Task added successfully!")

def remove_task(tasks, task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed successfully!")
    else:
        print("Task not found in the list.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def main():
    tasks = []

    while True:
        print("\nChoose any one option:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(tasks, task)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

