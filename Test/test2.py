# To take a directory input from the user and cd into it from a PowerShell command using Python
import subprocess
import os
#Input
dir = input("Enter the directory you want to enter into: ")
#Running cd
a = subprocess.run(["powershell", "-Command", f"cd '{dir}'; pwd"], capture_output=True, text=True)
print("Standard Output: ", a.stdout.strip())
print("Standard Error: ", a.stderr.strip())