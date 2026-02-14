import os

tasks = []

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
        print("Tasks loaded successfully!")

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print("Tasks saved to file.")

def show_tasks():
    if not tasks:
        print("\nYour task list is empty.")
    else:
        print("\nCurrent Tasks")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")

def add_task():
    task_name = input("Enter the task name: ")
    tasks.append(task_name)
    print(f"Added: {task_name}")

def remove_task():
    show_tasks()
    if tasks:
        try:
            choice = int(input("Enter the task number to remove: "))
            if 1 <= choice <= len(tasks):
                removed = tasks.pop(choice - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    load_tasks()
    
    while True:
        print("\n1. View Tasks | 2. Add Task | 3. Remove Task | 4. Save | 5. Exit")
        choice = input("Select an option (1-4): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            save_tasks()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
