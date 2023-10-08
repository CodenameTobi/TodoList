task_dict_model = {
    "name" : "Task",
    "description" : "This is an example task",
    "due_date" : "yyyy/mm/dd , hh/mm",
    "status" : "incomplete"
}

def get_tasks_from_databank(file):
    print("Getting tasks from databank: " + file)
    with open(file) as file:    
        tasks = file.read()
        print(tasks)

def update_databank(file, updated_tasks):
    print("Updating tasks in databank")


def add_task(task, databank):
    print("Adding one task")

def display_tasks():
    print("Displaying all tasks")

def complete_task():
    print("Task completed")

def delete_task(task):
    print("Delete Task")


def main():
    tasks = get_tasks_from_databank(r"taskData/todo.txt")
    
if __name__ == "__main__":
    main()