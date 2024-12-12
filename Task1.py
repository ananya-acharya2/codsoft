

def calculator():
    print("Calculator")
    print("Choose an option:")
    print("Addition")
    print("Subtraction")
    print("Multiplication")
    print("Division")

    try:
        operation = int(input("\nEnter the operation number"))

        if operation not in [1, 2, 3, 4]:
            print("Invalid operation choice")
            return

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == 1:
            result = num1 + num2
            print(f"\nResult: {num1} + {num2} = {result}")
        elif operation == 2:
            result = num1 - num2
            print(f"\nResult: {num1} - {num2} = {result}")
        elif operation == 3:
            result = num1 * num2
            print(f"\nResult: {num1} * {num2} = {result}")
        elif operation == 4:
            if num2 != 0:
                result = num1 / num2
                print(f"\nResult: {num1} / {num2} = {result}")
            else:
                print("\nError: Division by zero is not allowed.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()
