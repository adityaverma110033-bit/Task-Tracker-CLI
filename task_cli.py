import json  # Using json file to store tasks
import os  # Used to check if the database file (tasks.json) exists on the system
from datetime import datetime  # Tracks the time of task update and Task creation
import sys  # This one helps to read command line arguments

if not os.path.exists('tasks.json'):  # checkif json file exists
    with open('tasks.json', 'w') as f: # if json file not exists create one
        json.dump([], f)

def load_tasks():
    try:
        with open("tasks.json", "r") as f: # loads data from json file
            return json.load(f)
            
    except json.JSONDecodeError:
        # This runs if the file exists but is empty or "broken"
        print("Warning: tasks.json was empty or corrupted. Resetting to []")
        return []
  
def add(task):  
    tasks = load_tasks()  # storing data in tasks variable
    now = datetime.now().strftime("%b %d, %H:%M:%S")  # storing date and time in now variable
    if len(tasks) >= 1:
        ID = tasks[len(tasks)-1]["ID"] + 1    # create unique 'ID' for every task added
    else:
        ID = 1
    tasks.append({"ID":ID , "Description":task , "status":"todo" ,"createdAt": now ,"updatedAt": now})
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent = 4)   # store added tasks in json file 
    print(f"Task added successfully (ID = {ID})")

def update(task_ID , new_task):
    tasks = load_tasks()
    found = False 
    for task in tasks:
        if task["ID"] == task_ID: # check if task ID found in json file
            task["Description"] = new_task # if found update task
            task["updatedAt"] = datetime.now().strftime("%b %d, %H:%M:%S") # update time when task is updated
            found = True
            with open("tasks.json", "w") as f:
                json.dump(tasks, f, indent = 4)
                print(f"Task {task_ID} updated successfully")
                break
    if not found:
        print(f"Task with ID {task_ID} not found") # if ID not matched print task ID not found

def delete(task_ID):
    tasks = load_tasks()
    found = False
    for task in tasks:
        if task["ID"] == task_ID:
            tasks.remove(task)  # remove task if task ID found
            found = True
            with open("tasks.json", "w") as f:
                json.dump(tasks, f, indent = 4)  # update the json file
                print(f"Task {task_ID} deleted succesfully")
                break

    if not found:
        print(f"Task with ID {task_ID} not found")

def mark(task_tag , task_ID):
    valid_status = ["todo", "in-progress", "done"]
    valid_tag = task_tag.lower() # converting tag in lower case
    if valid_tag not in valid_status: # check if given tag is incorrect
        print(f"Error: '{task_tag}' is not a valid status.")
        print("Please use: todo, in-progress, or done.")
        return
    tasks = load_tasks()
    found = False
    for task in tasks:
        if task["ID"] == task_ID:
            task["status"] = valid_tag  # update the existing tag
            task["updatedAt"] = datetime.now().strftime("%b %d, %H:%M:%S") # update time
            found = True
            with open("tasks.json", "w") as f:
                json.dump(tasks, f, indent = 4) # update json file with new data
                print(f"Task {task_ID} marked as {valid_tag}")
                break
    if not found:
        print(f"Task with ID {task_ID} not found")

def list_all():
    tasks = load_tasks()
    if not tasks: # check if json file is empty
        print("Your task list is completely empty.")
        return
    print("\n" + "=" * 40)
    print((" " * 15) + "ALL TASKS")
    print("=" * 40)
    for task in tasks: # list every task in json file
        print(f"{task['ID']:<5} {task['Description']:<20} ({task['status'].upper()})")
    print("=" * 40 + "\n")



def list_tasks(task_status):
    valid_status = ["todo", "in-progress", "done"]
    valid_tag = task_status.lower()
    if valid_tag not in valid_status: #check if tag is valid
        print(f"Error: '{task_status}' is not a valid status.")
        print("Please use: todo, in-progress, or done.")
        return  
    tasks = load_tasks()
    if not tasks:
        print("Your task list is completely empty.")
        return
    found = False
    print("\n" + "=" * 40)
    print(" " * 15 + valid_tag.upper())
    print("=" * 40)
    for task in tasks: # list tasks having similar tag, (eg.in-progress)
        if task["status"] == valid_tag:
            print(f"{task['ID']:<5} {task['Description']}")
            found = True
    print("=" * 40 + "\n")
    if not found:  
        print("No tasks found.")

def info_task(task_id):
    tasks = load_tasks()
    for task in tasks: # find task having similar ID given by user
        if task["ID"] == task_id: # if found list every detail
            print("\n" + "="*40)
            print(f"TASK DETAILS (ID: {task['ID']})")
            print("="*40)
            print(f"Description:  {task['Description']}")
            print(f"Status:       {task['status'].upper()}")
            print(f"Created At:   {task['createdAt']}")
            print(f"Updated At:   {task['updatedAt']}")
            print("="*40 + "\n")
            return
            
    print(f"Error: Task with ID {task_id} not found.") # if not found print 'statement'

def show_help():  # help function
    print("\n" + "="*65)
    print(" "*20 + "TASK TRACKER CLI - HELP")
    print("="*65)
    print(" "*25 + "COMMANDS")
    print("="*65)
    print('  add "task Description"          (Add a new task)')
    print('  update ID "new Description"     (Update task by ID)')
    print("  delete ID                       (Remove a task)")
    print("  mark-in-progress ID             (Change status)")
    print("  mark-done ID                    (Finish task)")
    print("  list                            (Show all)")
    print("  list status                     (show tasks having same status)")
    print("  info ID                         (View complete task details)")
    print("  help                            (Show this menu)")
    print("="*65 + "\n")

def main():
    # Check if the user provided at least one command
    if len(sys.argv) < 2:  # check if user have not given any task
        show_help()  # calling help function for user convenience
        return
    
    command = sys.argv[1].lower() # convert commands in lower case for execution

    # 1. ADD COMMAND
    if command == "add":
        if len(sys.argv) < 3: # check if user give a task
            print("Error: Please provide a task description.")
        else:
            add(sys.argv[2]) # if given add task

    # 2. UPDATE COMMAND
    elif command == "update":
        if len(sys.argv) < 4: # check if user give 'ID' and also give task
            print("Usage: update [ID] [New Description]")
        else:
            update(int(sys.argv[2]), sys.argv[3]) # if given update task

    # 3. DELETE COMMAND
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: delete [ID]")
        else:
            delete(int(sys.argv[2]))

    # 4. MARK COMMANDS
    elif command == "mark-in-progress":
        mark("in-progress", int(sys.argv[2])) # if command is correct update task status
    elif command == "mark-done":
        mark("done", int(sys.argv[2]))

    # 5. LIST COMMANDS
    elif command == "list":
        # Check if user want a filtered list (e.g., 'list done')
        if len(sys.argv) > 2:
            list_tasks(sys.argv[2])
        else:
            list_all() # list every task

    # 6. INFO COMMAND
    elif command == "info":
        if len(sys.argv) < 3: 
            print("Usage: info [ID]")
        else:
            info_task(int(sys.argv[2])) # gives info of a particular task
    
    # 7. HELP COMMMAND
    elif command == "help": # check if user asked for help
        show_help() # call help function
    else:
        print(f"Unknown command: '{command}'") # if command is not valid for execution print 'statement'

if __name__ == "__main__":
    main()



