
DATABANK = r"taskData/todo.txt"

def clear_databank(databank):
    open(databank, 'w').close()        

def add_task(databank):
    clear_databank(databank)
    name, description, due_date = get_task_from_user()
    with open(databank, 'a') as db:
        db.write("\n" + "-" * 100 + "\n")
        db.write("Name:\t\t" + name + "\n")
        db.write("Description:\n\t\t" + description + "\n")
        db.write("Due Date:\t" + due_date + "\n")
        db.write("Status:\t\tincomplete\n")
        db.write("-" * 100 + "\n")


def get_task_from_user():
    taskDict = {'name' : False}
    taskDict['name'] = input("What is the name of the task?: ")
    taskDict['description'] = input("Add a description to your task:\n")
    taskDict['due_date'] = input("When is your task due? (dd/mm/yyyy,hh:mm)\n")
    return taskDict['name'], taskDict['description'], taskDict['due_date']

def display_tasks(databank):
    with open(databank) as db:
        display_tasks = db.read()
        print(display_tasks) 

def complete_task():
    # TODO: maybe
    print("Task completed")


def delete_task(task):
    # TODO
    print("Delete Task")

def delete_all(databank):
    # all tasks in the databank are deleted
    print("Deleting all tasks out of " + databank + "\n")
    with open(databank, 'w') as db:
        db.write("Empty")

def menu():
    # this function handles the user interaction
    # this includes adding task, displaying tasks, deleting tasks and updating them
    choice, min_value, max_value = (1000, 0, 4)
    menu_header = "-" * 8 + "Main menu" + "-" * 22
    menu_options = "\t[0] - Exit\n" \
                    "\t[1] - Add task\n" \
                    "\t[2] - Display tasks\n" \
                    "\t[3] - Delete task\n" \
                    "\t[4] - Delete all tasks\n"
    menu_end = "-" * 39
    print(menu_header + "\n" + menu_options + menu_end)
    while choice < min_value or choice > max_value:
        try:
            choice = int(input("Enter a number between " + str(min_value) + " and " + str(max_value) + " : "))
        except:
            print("NO VALID CHOICE")
    return choice


def main():
    # tasks = get_tasks_from_databank(r"taskData/todo.txt")
    exit = True
    while exit != 0:
        exit = menu()
        if exit == 0:
            continue
        elif exit == 1:
            # Add task
            print("Add task")
            add_task(DATABANK)
        elif exit == 2:
            # Display tasks
            print("Display tasks")
            display_tasks(DATABANK)
        elif exit == 3:
            # Delete task
            print("Delete task")
        elif exit == 4:
            print("Delete all tasks")
            delete_all(DATABANK)
        else:
            print("This has not been implemented yet!")

    print("Todo List closed")
    
if __name__ == "__main__":
    main()