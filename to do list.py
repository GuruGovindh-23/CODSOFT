todo_list = []

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")

def view_todo_list():
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(todo_list, start=1):
            status = "Completed" if task['completed'] else "Pending"
            print(f"{i}. {task['title']} - {status}")

def add_task():
    title = input("\nEnter the task title: ")
    task = {'title': title, 'completed': False}
    todo_list.append(task)
    print(f"Task '{title}' added to the to-do list.")

def update_task():
    view_todo_list()
    task_number = int(input("\nEnter the task number to update: "))
    if 1 <= task_number <= len(todo_list):
        new_title = input("Enter the new task title: ")
        todo_list[task_number - 1]['title'] = new_title
        print(f"Task {task_number} updated to '{new_title}'.")
    else:
        print("Invalid task number.")

def delete_task():
    view_todo_list()
    task_number = int(input("\nEnter the task number to delete: "))
    if 1 <= task_number <= len(todo_list):
        removed_task = todo_list.pop(task_number - 1)
        print(f"Task '{removed_task['title']}' deleted from the to-do list.")
    else:
        print("Invalid task number.")

def mark_task_completed():
    view_todo_list()
    task_number = int(input("\nEnter the task number to mark as completed: "))
    if 1 <= task_number <= len(todo_list):
        todo_list[task_number - 1]['completed'] = True
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number.")
        
def main():
    while True:
        show_menu()
        choice = input("\nChoose an option: ")
        
        if choice == '1':
            view_todo_list()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            mark_task_completed()
        elif choice == '6':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a valid option.")

if __name__ == "__main__":
    main()
