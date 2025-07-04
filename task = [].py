task = []
def add_task(task):
    task.append(task)
    print("Task added successfully!")

def remove_task(task):
    if task in task:
        task.remove(task)
        print("Task removed successfully!")
    else:
        print("Task not found.")

def view_task():
    if not task:
        print("no tasks to display.")
    else:
        for i,task in enumerate(task):
        print(f"{i+1}. {task}")

while True:
    print("menu:")
    print("1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Quit")


choice = input("enter your choice:")

    if choice == "1":
        task = input("enter the task:")
        add_task(task)
    elif choice == "2":
        task = input("enter the task to remove:")
        remove_task(task)
    elif choice == "3":
        view_task()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. please try again.")