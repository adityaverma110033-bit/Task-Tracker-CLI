import json  # Using json file to store tasks
import os  # Used to check if the database file (tasks.json) exists on the system
from datetime import datetime  # Tracks the time of task update and Task creation
import sys  # This one helps to read command line arguments

# Import Colorama for cross-platform terminal styling
try:
    from colorama import init, Fore, Style
    init(autoreset=True)  # Automatically resets style after each print
except ImportError:
    # Fallback to plain text if colorama isn't installed locally yet
    class FakeColor:
        def __getattr__(self, name): return ""
    Fore = Style = FakeColor()

if not os.path.exists('tasks.json'):  # check if json file exists
    with open('tasks.json', 'w') as f: # if json file not exists create one
        json.dump([], f)

def load_tasks():
    try:
        with open("tasks.json", "r") as f: # loads data from json file
            return json.load(f)
    except json.JSONDecodeError:
        print(Fore.RED + "Warning: tasks.json was empty or corrupted. Resetting to []")
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
    print(Fore.GREEN + f"✔ Task added successfully (ID = {ID})")

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
                print(Fore.GREEN + f"✔ Task {task_ID} updated successfully")
                break
    if not found:
        print(Fore.RED + f"✘ Task with ID {task_ID} not found") # if ID not matched print task ID not found

def delete(task_ID):
    tasks = load_tasks()
    found = False
    for task in tasks:
        if task["ID"] == task_ID:
            tasks.remove(task)  # remove task if task ID found
            found = True
            with open("tasks.json", "w") as f:
                json.dump(tasks, f, indent = 4)  # update the json file
                print(Fore.RED + f"🗑 Task {task_ID} deleted successfully")
                break
    if not found:
        print(Fore.RED + f"✘ Task with ID {task_ID} not found")

def mark(task_tag , task_ID):
    valid_status = ["todo", "in-progress", "done"]
    valid_tag = task_tag.lower() # converting tag in lower case
    if valid_tag not in valid_status: # check if given tag is incorrect
        print(Fore.RED + f"Error: '{task_tag}' is not a valid status.")
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
                print(Fore.GREEN + f"✔ Task {task_ID} marked as {valid_tag}")
                break
    if not found:
        print(Fore.RED + f"✘ Task with ID {task_ID} not found")

def list_all():
    tasks = load_tasks()
    if not tasks: # check if json file is empty
        print(Fore.YELLOW + "Your task list is completely empty.")
        return
    print(Fore.CYAN + "\n" + "=" * 45)
    print(Fore.CYAN + (" " * 17) + "ALL TASKS")
    print(Fore.CYAN + "=" * 45)
    for task in tasks: # list every task in json file
        status = task['status'].upper()
        # Custom status coloring
        if task['status'] == 'done':
            status_str = Fore.GREEN + f"({status})"
        elif task['status'] == 'in-progress':
            status_str = Fore.YELLOW + f"({status})"
        else:
            status_str = Fore.LIGHTWHITE_EX + f"({status})"
            
        print(f"{Fore.LIGHTBLUE_EX}{task['ID']:<5} {Fore.WHITE}{task['Description']:<25} {status_str}")
    print(Fore.CYAN + "=" * 45 + "\n")

def list_tasks(task_status):
    valid_status = ["todo", "in-progress", "done"]
    valid_tag = task_status.lower()
    if valid_tag not in valid_status: #check if tag is valid
        print(Fore.RED + f"Error: '{task_status}' is not a valid status.")
        print("Please use: todo, in-progress, or done.")
        return  
    tasks = load_tasks()
    if not tasks:
        print(Fore.YELLOW + "Your task list is completely empty.")
        return
    found = False
    print(Fore.CYAN + "\n" + "=" * 45)
    print(Fore.CYAN + " " * 18 + valid_tag.upper())
    print(Fore.CYAN + "=" * 45)
    for task in tasks: # list tasks having similar tag, (eg.in-progress)
        if task["status"] == valid_tag:
            print(f"{Fore.LIGHTBLUE_EX}{task['ID']:<5} {Fore.WHITE}{task['Description']}")
            found = True
    print(Fore.CYAN + "=" * 45 + "\n")
    if not found:  
        print(Fore.YELLOW + "No tasks found.")

def info_task(task_id):
    tasks = load_tasks()
    for task in tasks: # find task having similar ID given by user
        if task["ID"] == task_id: # if found list every detail
            print(Fore.BLUE + "\n" + "="*45)
            print(Fore.BLUE + f"TASK DETAILS (ID: {task['ID']})")
            print(Fore.BLUE + "="*45)
            print(f"{Fore.WHITE}Description:  {Fore.LIGHTWHITE_EX}{task['Description']}")
            
            status = task['status'].upper()
            color = Fore.GREEN if task['status'] == 'done' else (Fore.YELLOW if task['status'] == 'in-progress' else Fore.WHITE)
            
            print(f"{Fore.WHITE}Status:       {color}{status}")
            print(f"{Fore.WHITE}Created At:   {Fore.LIGHTBLACK_EX}{task['createdAt']}")
            print(f"{Fore.WHITE}Updated At:   {Fore.LIGHTBLACK_EX}{task['updatedAt']}")
            print(Fore.BLUE + "="*45 + "\n")
            return
            
    print(Fore.RED + f"Error: Task with ID {task_id} not found.") # if not found print 'statement'

def show_help():  # help function
    print(Fore.MAGENTA + "\n" + "="*65)
    print(Fore.MAGENTA + " "*20 + "TASK TRACKER CLI - HELP")
    print(Fore.MAGENTA + "="*65)
    print(" "*25 + "COMMANDS")
    print(Fore.MAGENTA + "="*65)
    print(f"  {Fore.GREEN}add {Fore.WHITE}\"task Description\"          {Fore.LIGHTBLACK_EX}(Add a new task)")
    print(f"  {Fore.GREEN}update {Fore.BLUE}ID {Fore.WHITE}\"new Description\"     {Fore.LIGHTBLACK_EX}(Update task by ID)")
    print(f"  {Fore.GREEN}delete {Fore.BLUE}ID                       {Fore.LIGHTBLACK_EX}(Remove a task)")
    print(f"  {Fore.GREEN}mark-in-progress {Fore.BLUE}ID             {Fore.LIGHTBLACK_EX}(Change status to working)")
    print(f"  {Fore.GREEN}mark-done {Fore.BLUE}ID                    {Fore.LIGHTBLACK_EX}(Finish task)")
    print(f"  {Fore.GREEN}list                            {Fore.LIGHTBLACK_EX}(Show all)")
    print(f"  {Fore.GREEN}list {Fore.YELLOW}status                     {Fore.LIGHTBLACK_EX}(Show tasks filtered by status)")
    print(f"  {Fore.GREEN}info {Fore.BLUE}ID                         {Fore.LIGHTBLACK_EX}(View complete task details)")
    print(f"  {Fore.GREEN}help                            {Fore.LIGHTBLACK_EX}(Show this menu)")
    print(Fore.MAGENTA + "="*65 + "\n")

def main():
    if len(sys.argv) < 2:  # Check if user ran the tool completely blank
        show_help()  
        return
    
    command = sys.argv[1].lower()

    # 1. ADD COMMAND
    if command == "add":
        if len(sys.argv) < 3: 
            print(Fore.RED + "Error: Missing task description.")
            print(Fore.YELLOW + 'Usage: task-cli add "Your task description"')
        else:
            add(sys.argv[2]) 

    # 2. UPDATE COMMAND
    elif command == "update":
        if len(sys.argv) < 4: 
            print(Fore.RED + "Error: Missing operational arguments.")
            print(Fore.YELLOW + 'Usage: task-cli update [ID] "New Description"')
        else:
            try:
                update(int(sys.argv[2]), sys.argv[3]) 
            except ValueError:
                print(Fore.RED + "Error: ID must be a number.")
                print(Fore.YELLOW + 'Usage: task-cli update [ID] "New Description"')

    # 3. DELETE COMMAND
    elif command == "delete":
        if len(sys.argv) < 3:
            print(Fore.RED + "Error: Missing task ID.")
            print(Fore.YELLOW + 'Usage: task-cli delete [ID]')
        else:
            try:
                delete(int(sys.argv[2]))
            except ValueError:
                print(Fore.RED + "Error: ID must be a number.")
                print(Fore.YELLOW + 'Usage: task-cli delete [ID]')

    # 4. MARK COMMANDS
    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print(Fore.RED + "Error: Missing task ID.")
            print(Fore.YELLOW + 'Usage: task-cli mark-in-progress [ID]')
        else:
            try:
                mark("in-progress", int(sys.argv[2])) 
            except ValueError:
                print(Fore.RED + "Error: ID must be a number.")
                print(Fore.YELLOW + 'Usage: task-cli mark-in-progress [ID]')
                
    elif command == "mark-done":
        if len(sys.argv) < 3:
            print(Fore.RED + "Error: Missing task ID.")
            print(Fore.YELLOW + 'Usage: task-cli mark-done [ID]')
        else:
            try:
                mark("done", int(sys.argv[2]))
            except ValueError:
                print(Fore.RED + "Error: ID must be a number.")
                print(Fore.YELLOW + 'Usage: task-cli mark-done [ID]')

    # 5. LIST COMMANDS
    elif command == "list":
        if len(sys.argv) > 2:
            list_tasks(sys.argv[2])
        else:
            list_all() 

    # 6. INFO COMMAND
    elif command == "info":
        if len(sys.argv) < 3: 
            print(Fore.RED + "Error: Missing task ID.")
            print(Fore.YELLOW + 'Usage: task-cli info [ID]')
        else:
            try:
                info_task(int(sys.argv[2])) 
            except ValueError:
                print(Fore.RED + "Error: ID must be a number.")
                print(Fore.YELLOW + 'Usage: task-cli info [ID]')
    
    # 7. HELP COMMMAND
    elif command == "help": 
        show_help() 
        
    # 8. COMPLETELY UNKNOWN COMMAND
    else:
        print(Fore.RED + f"Unknown command: '{command}'") 
        print(Fore.YELLOW + "Type 'task-cli help' to see all available commands.")

if __name__ == "__main__":
    main()