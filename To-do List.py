import json
from datetime import datetime

Task_File = 'tasks.json'
def load_tasks():
    try:
        with open(Task_File, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_tasks(tasks):
    with open(Task_File, 'w') as file:
        json.dump(tasks, file, indent=4)
def add_task(description, deadline=None):
    tasks = load_tasks()
    new_task = {
        'description': description,
        'deadline': deadline,
        'completed': False,
        'created_at': str(datetime.now())
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added!")
def list_tasks():
    tasks = load_tasks()
    for idx, task in enumerate(tasks, 1):
        status = "Done" if task['completed'] else "Pending"
        print(f"{idx}. {task['description']} - {status} (Deadline: {task.get('deadline', 'None')})")
def complete_task(task_index):
    tasks = load_tasks()
    if 0 < task_index <= len(tasks):
        tasks[task_index - 1]['completed'] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task number!")
def main():
    while True:
        print("\n1. Add Task\n2. List Tasks\n3. Mark Task as Complete\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            deadline = input("Enter deadline (YYYY-MM-DD) (optional): ") or None
            add_task(description, deadline)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            list_tasks()
            task_index = int(input("Enter task number to mark as complete: "))
            complete_task(task_index)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
                         







                            

            
