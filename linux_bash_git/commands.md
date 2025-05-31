# 🧠 Commands

## 🐙 Git Commands

| No. | Command                                                                | Description                                                               |
| --- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| 1   | `git init`                                                             | Initialize Git in this folder.                                            |
| 2   | `git add .`                                                            | Stage all files for Git.                                                  |
| 3   | `git commit -m "Commit Message"`                                       | Save a commit with a message.                                             |
| 4   | `git remote add origin git@github.com:your_git_username/repo_name.git` | Link local folder to your GitHub repo.                                    |
| 5   | `git branch -M main`                                                   | Rename the branch to `main`.                                              |
| 6   | `git push -u origin main`                                              | Push everything to GitHub.                                                |
| 7   | `git status`                                                           | See what's going on in Git (status check).                                |
| 8   | `git fetch`                                                            | Pulls down any changes from the remote repo (like updates to branches).   |
| 9   | `git pull`                                                             | Fetches and merges latest changes from remote repo.                       |
| 10  | `git pull --rebase`                                                    | Fetches changes then rebases your local commits on top.                   |                |
| 11  | `git push`                                                             | Send your changes to GitHub.                                              |
| 12  | `git config core.autocrlf true`                                        | If true, avoids line ending conflicts in unix and windows and vice-versa. |

## 🐚 Bash/Linux Commands

| No. | Command                               | Description                                                                                        |
| --- | ------------------------------------- | -------------------------------------------------------------------------------------------------- |
| 1   | `cd ~/projects`                       | Go to your WSL `projects` folder.                                                                  |
| 2   | `mkdir ~/projects`                    | Create the folder if it doesn't exist.                                                             |
| 3   | `mkdir weather-wizard`                | Make a new folder for your project.                                                                |
| 4   | `cd weather-wizard`                   | Move into that project folder.                                                                     |
| 5   | `touch main.py`                       | Create an empty Python file.                                                                       |
| 6   | `echo "# Weather Wizard" > README.md` | Make a simple README file.                                                                         |
| 7   | `wsl`                                 | Open the Ubuntu terminal from Windows (if not already inside).                                     |
| 8   | `cd ~/projects/python`                | Navigate to your Python project inside WSL.                                                        |
| 9   | `code .`                              | Open current folder in VS Code (using Remote - WSL magic).                                         |
| 10  | `command_1 && command_2`              | Executes multiple commands in sequence only if the previous command executes successfully.         |
| 11  | `command_1 ; command_2`               | Executes multiple commands in sequence even if the previous command fails to execute successfully. |
| 12  | `ls`                                  | Lists files and directories in the current location.                                               |
| 13  | `cp`                                  | Copies files or directories.                                                                       |
| 14  | `cd Directory_Name`                   | Changes directory to Directory\_Name.                                                              |
| 15  | `cd ..`                               | Changes directory to the parent directory.                                                         |
| 16  | `cd`                                  | Changes directory to the supreme parent directory \[do not run in GitHub Codespaces].              |
| 17  | `rm`                                  | Removes (deletes) a file.                                                                          |
| 18  | `rm -r`                               | Removes a directory and its contents recursively.                                                  |
| 19  | `mv`                                  | Moves or renames files or directories.                                                             |
| 20  | `mkdir`                               | Creates a new directory.                                                                           |
| 21  | `rmdir`                               | Removes an empty directory.                                                                        |
| 22  | `touch`                               | Creates a new empty file.                                                                          |
| 23  | `echo`                                | Prints text or variables to the terminal.                                                          |
| 24  | `exit`                                | Exits the shell.                                                                                   |
| 25  | `history`                             | Shows the list of previously run commands.                                                         |
| 26  | `man`                                 | Displays the manual/help for a command.                                                            |
| 27  | `chmod`                               | Changes file permissions.                                                                          |
| 28  | `bash`                                | Starts a new bash shell.                                                                           |
| 29  | `clear`                               | Clears the terminal screen; Shortcut: Ctrl+L.                                                      |
| 30  | `ctrl + c`                            | Stops the running process.                                                                         |
| 31  | `kill`                                | Terminates a process by PID.                                                                       |
| 32  | `./script_name.sh`                    | Running a sh script in vs code.                                                                |
| 33  | `chmod +x gitpush.sh`                 | Command to give rights to "gitpush.sh" script.                                                     |
| 34  | `pwd`                                 | To see your current working directory.                                                             |
| 35  | `mkdir -p parent/child1/`             | Creates all parent directories as needed doesn’t error out if some directories already exist.      |

## 🧰 System & VS Code Commands

| No. | Command                             | Description                                             |
| --- | ----------------------------------- | ------------------------------------------------------- |
| 1   | `uname -a`                          | Shows all system info like kernel, architecture, etc.   |
| 2   | `lsb_release -a`                    | Displays detailed Linux distro info.                    |
| 3   | `Remote: Close Remote Connection`   | Closes active VS Code remote session (like SSH/WSL).    |
| 4   | `WSL: Connect to WSL in New Window` | Opens a new VS Code window linked to your WSL instance. |
| 5   | `code .`                            | Opens the current folder in VS Code.                    |
| 6   | `wsl`                               | Open Ubuntu.                                            |
| 7   | `#Comment`                          | This is a comment after a "#" symbol.                   |
