import sys
import os
import sys
def main():
    """
    This function prompts the user for input and waits for user input.
    """



    # Wait for user input
    # If user types exit 0, exit the program
    # If user types echo, print the rest of the input
    # If user types type, print the type of the command
    # If user types an invalid command, print "command not found"
    PATH = os.environ.get("PATH")
    valid_commands = ["exit", "echo", "type", "pwd"]
    paths = PATH.split(":")
    while True:
        cmd_path = None
        sys.stdout.write("$ ")
        command = input().strip().split(" ")
        if command[0] not in valid_commands:
            if os.path.isfile(f"{command[0]}"):
                cmd_path = f"{command[0]}"
            if cmd_path:
                os.system(f"{' '.join(command)}")
            else:
                print(f"{command[0]}: command not found")
                continue
        if " ".join(command) == "exit 0":
            sys.exit(0)
        if command[0] == "echo":
            print(" ".join(command[1:]))
        if command[0] == "type":
            cmd_path = None
            paths = PATH.split(":")
            for path in paths:
                if os.path.isfile(f"{path}/{command[1]}"):  # Replace 'cmd' with 'command[1]'
                    cmd_path = f"{path}/{command[1]}"
            if(command[1] in valid_commands):
                print(f"{command[1]} is a shell builtin")
            else:
                if cmd_path:
                    print(f"{command[1]} is {cmd_path}")
                else:
                    print(f"{command[1]} not found")
        if command[0] == "pwd":
            print(f"{os.getcwd()}")





if __name__ == "__main__":
    main()
