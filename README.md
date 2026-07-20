#  Task Tracker CLI

A high-performance, and color-coded Command Line Interface (CLI) to seamlessly manage your daily tasks. Built with Python and compiled into a standalone binary, this tool requires **zero dependencies or programming setups** to run on your machine.

##  Features
- **Standalone Executable:** No Python installation, environment setup, or `pip` installation required. Just download and run.
- **Beautiful Visual Feedback:** Fully colorized interfaces utilizing custom board dividers and clear status tags for enhanced terminal readability.
- **Targeted Error Handling:** Smart usage guidance that catches incorrect syntax or missing arguments and prints an isolated instruction manual just for that specific operation.
- **Add & Update:** Effortlessly create tasks with descriptions or update existing ones by their unique ID.
- **Delete:** Permanently remove tasks from the database.
- **Track Status:** Transition and mark tasks cleanly as `todo`, `in-progress`, or `done`.
- **Metadata Tracking:** Automatically monitors and logs specific `createdAt` and `updatedAt` timestamps for every lifecycle change.
- **Filter & Info:** Instantly filter task views by status or view complete, deeply detailed metadata breakdowns of an individual task using its ID.
- **Persistent Storage:** Data automatically serializes into a clean, locally hosted `tasks.json` file inside the execution directory.

---

##  Installation & Global Setup

### Step 1: Download the Executable
1. Download the `task-cli-windows.zip` bundle from the release page.
2. Unzip the folder to extract the compiled standalone binary: `task-cli.exe`.

### Step 2: Enable Global Access (Recommended)
To run the `task-cli` command seamlessly from any directory or terminal workspace on your computer without having to type the `.\` file prefix, add the file to your System PATH:

1. Move the `task-cli.exe` file into a permanent, dedicated directory (e.g., `C:\Program Files\task-cli\`).
2. Open your Windows Start Menu, search for **"Environment Variables"**, and select **Edit the system environment variables**.
3. Under the **System Variables** section, locate the **Path** variable and click **Edit**.
4. Click **New** on the right side of the editor and paste your dedicated directory path (`C:\Program Files\task-cli\`).
5. Click **OK** to save your changes and completely restart any active Command Prompts, PowerShell instances, or VS Code terminals.

---

##  Usage & Command Syntax

Once global access is configured, you can execute operations anywhere on your machine using the standard `task-cli` command structure:

| Action | Command | Description |
| :--- | :--- | :--- |
| **Help Menu** | `task-cli help` | Displays the full, colorized operational manual |
| **Add Task** | `task-cli add "Your task description"` | Creates a new task |
| **List All** | `task-cli list` | Displays all stored tasks in a structured table |
| **Filter View** | `task-cli list done` / `in-progress` / `todo` | Lists tasks filtered exclusively by their tag |
| **Update Text** | `task-cli update 1 "Your updated description"` | Revises the text description of a specific task ID |
| **Mark Progress** | `task-cli mark-in-progress 1` | Sets the target task status to active |
| **Mark Done** | `task-cli mark-done 1` | Completes the target task |
| **Inspect Meta** | `task-cli info 1` | Displays comprehensive timestamp and state records |
| **Delete Task** | `task-cli delete 1` | Permanently deletes a task from storage |

---

## 🧠 Interactive Error Guidance
If you ever execute a command with missing inputs or invalid arguments (such as omitting a description on an `add` command, passing an incorrect status key, or supplying a text string instead of a numerical ID), the application elegantly flags the exact issue. It outputs an isolated blueprint to get you back on track instantly:

```text
Error: ID must be a number.
Usage: task-cli update [ID] "New Description"