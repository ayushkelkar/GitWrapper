# Can I execute simple git --version command?
import subprocess
a = subprocess.run(["git", "--version"], capture_output=True, text=True)
print("Standard Output: ", a.stdout)
print("Standard Error : ", a.stderr)