def addTask(tasks):
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def listTasks(tasks):
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")

def deleteTask(tasks):
    listTasks(tasks)
    try:
        taskToDelete = int(input("Enter the # to delete: "))
        if 0 <= taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been removed.")
        else:
            print(f"Task #{taskToDelete} was not found.")
    except ValueError:
        print("Invalid input.")

def main():
    tasks = []
    print("Welcome to the to-do list app :)")
    while True:
        print("\nPlease select one of the following options:")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addTask(tasks)
        elif choice == "2":
            deleteTask(tasks)
        elif choice == "3":
            listTasks(tasks)
        elif choice == "4":
            print("Goodbye 👋👋")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
