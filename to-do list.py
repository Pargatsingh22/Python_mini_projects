def show_tasks(tasks):
    if not tasks:
        print("No tasks in your to-do list.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    print()

def add_task(tasks):
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f'"{task}" has been added to your list.')

def remove_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f'"{removed_task}" has been removed.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        print("Options: [1] View Tasks  [2] Add Task  [3] Remove Task  [4] Exit")
        option = input("Select an option: ")

        if option == '1':
            show_tasks(tasks)
        elif option == '2':
            add_task(tasks)
        elif option == '3':
            remove_task(tasks)
        elif option == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please choose again.")

if __name__ == "__main__":
    main()
