def perform_operations():
    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (addition, subtraction, multiplication, division): ")

        if operation == "addition":
            result = number1 + number2
        elif operation == "subtraction":
            result = number1 - number2
        elif operation == "multiplication":
            result = number1 * number2
        elif operation == "division":
            if number2 == 0:
                raise ValueError("Division by zero!")
            result = number1 / number2
        else:
            raise ValueError("Unknown operation!")

        print(f"Result: {result}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


perform_operations()
