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

# Prompts for the user to enter two numbers
# Perform the user's selected operation and displaying their result
# Adding a prompt for the user asking if they want to try again
