# Will execute a full git cycle
import os
import subprocess

# Taking input and entering into the directory
dir = input("Enter into the directory which you want: ")

# Changing working directory:
try:
    os.chdir(dir)
    print(f"Changed working directory to: {os.getcwd()}")
except Exception as exc:
    print("Failed to change Directory")
    exit(1)

# git add . 
add = subprocess.run(["git", "add", "."], capture_output=True, text=True)
print("Successfully Executed Step 1: git add .")
print(add.stdout.strip())
print(add.stderr.strip())

# git commit
msg = input("Enter the message for commit: ")
comm = subprocess.run(["git", "commit", "-m", msg], capture_output=True, text=True)
print("Successfully Executed Step 2: git commit -m", msg)
print(comm.stdout.strip())
print(comm.stderr.strip())

# git push
push = subprocess.run(["git", "push"], capture_output=True, text=True)
print("Succesfully Executed Final Step: git push")
print(push.stdout.strip())
print(push.stderr.strip())