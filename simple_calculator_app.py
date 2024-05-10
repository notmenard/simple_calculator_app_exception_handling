# Displaying the introduction for the simple calculator application
while True:
    print(" Simple Calculator App ".center(73, "-"))
    print()

    # Displaying the list of operations on the calculator
    print("Choose an operation to be executed:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print()

    # Prompts the user to enter their choice of operation
    while True:
        try:
            choice = input("Enter operation of your choice (1-4): ")
            if choice not in ["1", "2", "3", "4"]:
                raise ValueError("Invalid choice. Please choose a valid option.")
            break
        except Exception as e:
            print(e)
            print("An unexpected error occurred. Please try the application again.")

    # Prompts for the user to enter two numbers
    while True:
        try:
            first_number = int(input("Enter first number: "))
            second_number = int(input("Enter second number: "))
            print()
        except ValueError as e:
            print(e)
            print("Invalid input. Please enter a valid number.")
        else:
            # Perform the user's selected operation and displaying their result
            if choice == "1":
                result = (first_number + second_number)
                print(f"Result: {result}")
# Adding a prompt for the user asking if they want to try again
