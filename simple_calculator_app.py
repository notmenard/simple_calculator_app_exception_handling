# Displaying the introduction for the simple calculator application
while True:
    print("\033[94m" + " Simple Calculator App ".center(73, "-") + "\033[0m")
    print()

    # Displaying the list of operations on the calculator
    print("\033[92m" + "Choose an operation to be executed:" + "\033[0m")
    print("\033[92m" + "1. Addition" + "\033[0m")
    print("\033[92m" + "2. Subtraction" + "\033[0m")
    print("\033[92m" + "3. Multiplication" + "\033[0m")
    print("\033[92m" + "4. Division" + "\033[0m")
    print()

    # Prompts the user to enter their choice of operation
    while True:
        try:
            choice = input("\033[92m" + "Enter operation of your choice (1-4): " + "\033[0m")
            if choice not in ["1", "2", "3", "4"]:
                raise ValueError("Invalid choice. Please choose a valid option.")
            break
        except Exception as e:
            print("\033[91m" + str(e) + "\033[0m")
            print("\033[91m" + "An unexpected error occurred. Please choose a valid option." + "\033[0m")

    # Prompts for the user to enter two numbers
    while True:
        try:
            first_number = int(input("\033[92m" + "Enter first number: " + "\033[0m"))
            second_number = int(input("\033[92m" + "Enter second number: " + "\033[0m"))
            print()
        except ValueError as e:
            print("\033[91m" + str(e) + "\033[0m")
            print("\033[91m" + "Invalid input. Please enter a valid number." + "\033[0m")
        else:
            break
    # Perform the user's selected operation and displaying their result
    if choice == "1":
        result = (first_number + second_number)
        print("\033[95m" + f"Result: {result}" + "\033[0m")
        print()
    elif choice == "2":
        result = (first_number - second_number)
        print("\033[95m" + f"Result: {result}" + "\033[0m")
        print()
    elif choice == "3":
        result = (first_number * second_number)
        print("\033[95m" + f"Result: {result}" + "\033[0m")
        print()
    elif choice == "4":
        try:
            result = (first_number // second_number)
            print("\033[95m" + f"Result: {result}" + "\033[0m")
            print()
        except ZeroDivisionError as e:
            print("\033[91m" + str(e) + "\033[0m")
            print("\033[91m" + "Invalid input. Please enter a valid number." + "\033[0m")
            print()

    # Adding a prompt for the user asking if they want to try again
    try_again = input("\033[92m" + "Do you want to try again? ('y' for yes / 'n' for no): " + "\033[0m")
    if try_again.lower() == 'y':
        continue
    elif try_again.lower() == 'n':
        print("\033[94m" + " Thank you for using the Simple Calculator App! ".center(73, "-") + "\033[0m")
        break
    else:
        print("\033[91m" + "Invalid choice. Please choose a valid option." + "\033[0m")
        