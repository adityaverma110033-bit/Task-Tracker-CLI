# 📝 Task Tracker CLI

A simple, efficient Command Line Interface (CLI) to manage your daily tasks, built with Python.

## 🚀 Features
- **Add** tasks with descriptions.
- **Update** existing tasks by ID.
- **Delete** tasks.
- **Track Status**: Mark tasks as `todo`, `in-progress`, or `done`.
- **created at**: tracks the record of when the task created.
- **updated at**: tracks the record of when the task was last updated.
- **Filter**: List tasks by their current status.
- **Persistent Storage**: All tasks are saved in a `tasks.json` file.
- **info**: Gives the info of any task accessing by its unique `ID`.


## 🛠️ Installation
1. **Clone the repository**:
   ```Bash
   git clone (https://github.com/your-username/Task-Tracker-CLI.git)


2. **Navigate to the folder**:
   ```Bash
   cd Task-Tracker-CLI

3. **Install globally**:
   pip install -e .

**NOTE**: Installation is done for adding alias "task-cli" to use CLI effectively reduce typing of lengthy commands to perform task.


**Alternative**: Running without Installation
If you prefer not to install the package globally, you can run the script directly using Python.
```PowerShell
   python task_cli.py add "Buy milk"

📖 Usage
 After installation, use the task-cli command:
 ACTION                     COMMAND
 Add Task	            task-cli add "Finish homework"
 List All	            task-cli list
 List Done	            task-cli list done
 Update	                task-cli update 1 "Finish math homework"
 Mark Progress	        task-cli mark-in-progress 1
 Delete	                task-cli delete 1
 info                   task-cli info 1
 help                   task-cli help

## 🔗 Project URL
View the source code and updates here: "https://github.com/adityaverma110033-bit/Task-Tracker-CLI"

