import sys
from datetime import datetime
from schemas.TaskSchema import PriorityLevel, Status
from modules.task import Task
from modules.manager import TaskManager

def show_menu():
    print("\n===== Task Management Application =====")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Update Task")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. Exit")

def list_tasks():
    tasks = TaskManager.list_tasks()
    if not tasks:
        print("\n⚠️ No tasks found.")
        return []

    print("\n📋 Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(
            f"{i}. [{task.status.value}] {task.title} "
            f"(Due: {task.due_date.date()}, Priority: {task.priority.value})"
        )
    return tasks

def add_task():
    title = input("Enter title: ")
    description = input("Enter description: ")
    due_date_str = input("Enter due date (YYYY-MM-DD): ")
    due_date = datetime.strptime(due_date_str, "%Y-%m-%d")

    priority_str = input("Enter priority (Low, Medium, High): ").capitalize()
    priority = PriorityLevel(priority_str) if priority_str in PriorityLevel._value2member_map_ else PriorityLevel.MEDIUM

    task = Task(
        title=title,
        description=description,
        due_date=due_date,
        priority=priority,
        status=Status.PENDING,
    )
    TaskManager.add_task(task)

def update_task():
    tasks = list_tasks()
    if not tasks:
        return

    task_num = int(input("Enter task number to update: "))
    if task_num < 1 or task_num > len(tasks):
        print("⚠️ Invalid task number")
        return

    task = tasks[task_num - 1]

    new_title = input(f"New title (leave blank to keep '{task.title}'): ") or task.title
    new_description = input(f"New description (leave blank to keep current): ") or task.description
    new_due_date_str = input(f"New due date (YYYY-MM-DD, leave blank to keep {task.due_date.date()}): ")
    new_due_date = datetime.strptime(new_due_date_str, "%Y-%m-%d") if new_due_date_str else task.due_date
    new_priority_str = input(f"New priority (Low, Medium, High, leave blank to keep {task.priority.value}): ")
    new_priority = PriorityLevel(new_priority_str.capitalize()) if new_priority_str else task.priority
    new_status_str = input(f"New status (Pending, In Progress, Completed, leave blank to keep {task.status.value}): ")
    new_status = Status(new_status_str) if new_status_str else task.status

    task.title = new_title
    task.description = new_description
    task.due_date = new_due_date
    task.priority = new_priority
    task.status = new_status

    TaskManager.update_task(task)

def complete_task():
    tasks = list_tasks()
    if not tasks:
        return

    task_num = int(input("Enter task number to mark complete: "))
    if task_num < 1 or task_num > len(tasks):
        print("⚠️ Invalid task number")
        return

    task = tasks[task_num - 1]
    TaskManager.complete_task(task.task_id)

def delete_task():
    tasks = list_tasks()
    if not tasks:
        return

    task_num = int(input("Enter task number to delete: "))
    if task_num < 1 or task_num > len(tasks):
        print("⚠️ Invalid task number")
        return

    task = tasks[task_num - 1]
    TaskManager.delete_task(task.task_id)

def main():
    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            complete_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("👋 Exiting Task Manager...")
            sys.exit(0)
        else:
            print("⚠️ Invalid choice, try again.")

if __name__ == "__main__":
    main()