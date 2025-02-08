def main():
    # Greet user
    print("Hello! Welcome to the program.")

    # Prompt user for command
    userInput = input("Enter a command: ").strip().lower()

    # Respond based on users input
    if userInput == "hello":
        print("Hi there!")
    elif userInput == "bye":
        print("Goodbye!")
    elif userInput == "how are you":
        print("I'm doing well, thank you!")
    else:
        print("I'm sorry, I don't recognize that command.")

if __name__ == '__main__':
    main()
