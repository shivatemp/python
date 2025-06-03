## GitHub SSH Setup - Essential Instructions (Steps 1 to 9)

This document provides a simplified, command-free instruction guide for connecting your local Git repository to GitHub via SSH using port 443. Follow these points to ensure a clean and successful setup.

---

### Step 1: Configure Git Identity

* Set your Git username and email to match your GitHub account.
* This ensures your commits are properly linked to your GitHub profile.
* Use global configuration unless working with multiple GitHub accounts.

### Step 2: Generate SSH Key

* Generate a new `ed25519` SSH key pair.
* Save it with a custom name to avoid conflicts with existing keys.
* Do not share your private key.

### Step 3: Add Public Key to GitHub

* Copy the contents of the public key file.
* Paste it into your GitHub account under SSH keys.
* Ensure the correct key is selected if you have multiple keys.

### Step 4: Configure SSH for Port 443

* Create or edit your SSH config file.
* Specify that connections to GitHub should use port 443.
* Point to the SSH key generated in Step 2.

### Step 5: Initialize Local Repository

* Navigate to your project folder.
* Run Git initialization to enable version tracking.
* Ensure `.git` is created in the folder.

### Step 6: Connect to Remote Repository

* Add your GitHub repository as the remote origin.
* Double-check the remote URL for typos.
* Use SSH URL format, not HTTPS.

### Step 7: Create Initial Commit

* Create at least one file to avoid empty repo issues.
* Stage the file and commit with a clear message.
* Use meaningful commit messages.

### Step 8: Rename Local Branch (If Needed)

* Check if your local branch is named `master`.
* If yes, rename it to `main` to match GitHub.
* This prevents push/pull mismatches.

### Step 9: Pull and Push

* If GitHub already contains data, pull with the flag to allow unrelated histories.
* Resolve any conflicts if they arise.
* Push your local branch to GitHub and set it to track the remote.

---

### General Tips:

* Always verify remote URLs before pushing.
* Check the current branch using `git branch`.
* Use `git status` frequently to monitor file states.
* Do not force push unless you're sure about overwriting remote history.
* Keep your SSH private key secure.

Following these steps will ensure a stable and secure Git to GitHub connection using SSH.
