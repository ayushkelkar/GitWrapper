# GitWrapper CLI v1.0
import os
import subprocess as sbp

# Defining a function to change directory.
def changedir():
    directory = input("Enter into the directory which you want to go into: ") 
    directory = os.path.normpath(directory)
    if not os.path.isdir(directory):
        print("Path you entered does not exist. Exiting.")
        return 1
    else:
        try:
            os.chdir(directory)
            print(f"Changed working directory to: {os.getcwd()}")
            return 0
        except Exception as ex1:
            print("Failed to Change Directory")
            return 2

# Defining a function for the command: git add
def add():
    msg1 = input("Do you want to only add a specific folder or not? [Y/N]")
    msg1 = msg1.lower().strip()
    if msg1 == 'y':
        msg2 = input("Enter the name of the folder you want to add:  WARNING: It is case-sensitive\n")
        msg2 = msg2.strip()
        msg2 = os.path.normpath(msg2)
        if not os.path.exists(msg2):
            print("Folder you entered does not exist. Exiting.")
            return 3
        else:
            addrslt = sbp.run(["git","add",msg2], capture_output=True, text=True)
        if addrslt.stderr.strip() == '':
            print("Command executed successfully. No errors.")
            print(addrslt.stdout.strip())
            return 0
        else:
            print("Command failed. Exiting.")
            print(addrslt.stderr.strip())
            return 4
    elif msg1 == 'n':
        print("Input accepted. Adding all folders to git.")
        addrslt = sbp.run(["git","add","."], capture_output=True, text=True)     
        if addrslt.stderr.strip() == '':
            print("Command executed successfully. No errors.")
            print(addrslt.stdout.strip())
            return 0
        else:
            print("Command Failed. Exiting.")
            print(addrslt.stderr.strip())
            return 5

# Defining a function for the command: git commit -m "Message"
def cmit():
    msg3 = input("Enter your commit message: \n")
    msg3 = msg3.strip()
    if msg3 == '':
        print("Empty commit message is forbidden. Exiting.")
        return 6
    else:
        cmitrslt =  sbp.run(["git","commit","-m",msg3], capture_output=True, text=True)
        if cmitrslt.stderr.strip() == '':
            print("Command executed successfully. No errors.")
            print(cmitrslt.stdout.strip())
            return 0
        else:
            print("Command Failed. Exiting. Error is given below:\n")
            print(cmitrslt.stderr.strip())
            return 7
        
# Defining a function for the command: git push
def psh():
    print("Executing git push...\n")
    pushrslt = sbp.run(["git","push"], capture_output=True, text=True)
    if pushrslt.returncode == 0:
        print("Command executed successfully. No errors.")
        print(pushrslt.stdout.strip())
        if pushrslt.stderr.strip():
            print("Note:\n",pushrslt.stderr.strip())
        return 0
    else:
        print("Command Failed. Exiting. Error is given below:\n")
        print(pushrslt.stderr.strip())
        return 8
    
# Defining a main function
def main():
    print("----------------------- GitWrapper v1.0 -----------------------\n")
    print("----------------------- Step 1: Change Working Directory:- -----------------------\n")
    rslt1 = changedir()
    if rslt1 != 0:
        print("Directory Change Failed. Exiting.")
        return
    print("\n----------------------- Step 2: git add -----------------------\n")
    rslt2 = add()
    if rslt2 != 0:
        print("Function failed. Exiting.")
        return
    print("\n----------------------- Step 3: git commit -----------------------\n")
    rslt3 = cmit()
    if rslt3 != 0:
        print("Commit Failed. Exiting.")
        return
    print("\n----------------------- Step 4: git push -----------------------\n")
    rslt4 = psh()
    if rslt4 != 0:
        print("Commit(s) failed. Exiting.")
    else:
        print("----------------------- Push Successful! -----------------------")
        input("\nPress Enter to exit...")
    
# Fallback incase I import this somewhere else
if __name__ == "__main__":
    main()