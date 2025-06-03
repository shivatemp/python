## Complete Guide: Connecting Git to GitHub via SSH on Port 443 (Windows)

This guide outlines the full process of setting up Git on a Windows machine, generating an SSH key (using `ed25519`), configuring SSH to use port 443, and linking a local repository to a GitHub remote.

---

### Prerequisites

* Git for Windows installed
* Git Bash available
* A GitHub account
* A GitHub repository already created

---

## Step-by-Step Instructions

### **Step 1: Configure Git User Information**

#### Command:

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

#### Verify:

```bash
git config --global --list
```

#### Expected Output:

```
user.name=Your Name
user.email=your_email@example.com
```

---

### **Step 2: Generate SSH Key**

#### Command:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com" -f ~/.ssh/github_ed25519
```

* Press Enter when prompted for passphrase (optional).
* This creates:

  * Private key: `~/.ssh/github_ed25519`
  * Public key: `~/.ssh/github_ed25519.pub`

---

### **Step 3: Add SSH Key to GitHub**

#### Command:

```bash
cat ~/.ssh/github_ed25519.pub
```

* Copy the output.
* Go to GitHub > Settings > SSH and GPG keys > New SSH key
* Paste the key and save.

---

### **Step 4: Configure SSH to Use Port 443**

#### Command (Git Bash):

```bash
notepad ~/.ssh/config
```

#### Content to Add:

```
Host github.com
  HostName ssh.github.com
  User git
  Port 443
  IdentityFile ~/.ssh/github_ed25519
```

#### Test Connection:

```bash
ssh -T git@github.com
```

#### Expected Output:

```
Hi your-github-username! You've successfully authenticated, but GitHub does not provide shell access.
```

---

### **Step 5: Initialize Local Git Repository**

#### Command:

```bash
cd /d/your-folder
mkdir your-project-folder
cd your-project-folder
git init
```

#### Expected Output:

```
Initialized empty Git repository in D:/your-folder/your-project-folder/.git/
```

---

### **Step 6: Add Remote Repository**

#### Command:

```bash
git remote add origin git@github.com:your-username/your-repo.git
git remote -v
```

#### Expected Output:

```
origin  git@github.com:your-username/your-repo.git (fetch)
origin  git@github.com:your-username/your-repo.git (push)
```

---

### **Step 7: Create Initial Commit**

#### Create a file:

```bash
echo "# Project Title" > README.md
```

#### Stage and Commit:

```bash
git add .
git commit -m "Initial commit"
```

#### Expected Output:

```
[main (root-commit) abc1234] Initial commit
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
```

---

### **Step 8: Rename Branch (if needed)**

#### Command:

```bash
git branch -M main
```

#### Verify:

```bash
git branch
```

#### Expected Output:

```
* main
```

---

### **Step 9: Pull and Push to GitHub**

#### If GitHub already has files (e.g., README):

```bash
git pull origin main --allow-unrelated-histories
```

* Resolve merge conflicts if prompted.

#### Then push:

```bash
git push -u origin main
```

#### Expected Output:

```
Enumerating objects: X, done.
To github.com:your-username/your-repo.git
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

---

### Final Notes

* Use `git status` to check file tracking state.
* Use `git log` to verify commit history.
* Subsequent pushes only require: `git push`

This concludes the setup process for connecting a local Git repo to GitHub over SSH using port 443.
