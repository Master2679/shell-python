import sys
def main():
    """
    This function prompts the user for input and waits for user input.
    """

    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    command = input()
    print(command + ": command not found\n")

if __name__ == "__main__":
    main()
