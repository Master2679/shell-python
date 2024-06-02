import sys
def main():
    """
    This function prompts the user for input and waits for user input.
    """



    # Wait for user input
    valid_commands = ["exit", "echo", "type"]
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input().strip().split(" ")
        if command[0] not in valid_commands:
            print(f"{command[0]}: command not found")
            continue
        if command[0] + " " + command[1] == "exit 0":
            sys.exit(0)
        if command[0] == "echo":
            print(" ".join(command[1:]))
        if command[0] == "type":
            if(command[1] in valid_commands):
                print(f"{command[1]} is a shell builtin")
            else:
                print(f"{command[1]} not found")





if __name__ == "__main__":
    main()
