import sys
def main():
    """
    This function prompts the user for input and waits for user input.
    """



    # Wait for user input
    valid_commands = ["exit 0"]
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        user_command = input()
        if user_command not in valid_commands:
            print(f"{user_command}: command not found")
            continue
        if user_command == "exit 0":
            break



if __name__ == "__main__":
    main()
