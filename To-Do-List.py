tasks = []
def add_task():
    task = input("Enter Task: ")
    while True:
        title = input("Enter Status (Pending/Completed): ").capitalize()
        if title in ['Pending', 'Completed']:
            break
        else:
            print("Invalid status. Please enter 'Pending' or 'Completed'.")
    if task and title:
        tasks.append(f"{task} - {title}")
        print("Task added successfully.")
        auto_save()
def auto_save():
    file_path = "E:/To-Do-List/Final Tasks.txt"
    with open(file_path, "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print("Tasks saved.")
def view_tasks():
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks available.")
def update_task():
    view_tasks()
    try:
        index_num = int(input("Enter task number to update: ")) - 1
        if index_num >= 0 and index_num < len(tasks):
            updated_title = input("Enter updated status (Pending/Completed): ").capitalize()
            if updated_title in ['Pending', 'Completed']:
                task_description = tasks[index_num].split(" - ")[0] #extract the 1st element of that str [0]-[1]
                tasks[index_num] = f"{task_description} - {updated_title}"
                print("Task status updated.")
                auto_save()
            else:
                print("Invalid status.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")
def delete_task():
    view_tasks()
    try:
        selected_index = int(input("Enter task number to delete: ")) - 1
        if selected_index >= 0 and selected_index < len(tasks):
            tasks.pop(selected_index)
            print("Task deleted.")
            auto_save()
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")
def menu():
    while True:
        print("\nTask Manager\n1. Add Task\n2. View Tasks\n3. Update Task\n4. Delete Task\n5. Exit")
        choice = input("Choose an option: ")
        if choice == '1': add_task()
        elif choice == '2': view_tasks()
        elif choice == '3': update_task()
        elif choice == '4': delete_task()
        elif choice == '5': 
            print("Tata Bye Bye Good Bye See You Later Buddy")
            break
        else: 
            print("Invalid choice.")
if __name__ == "__main__":
    menu()