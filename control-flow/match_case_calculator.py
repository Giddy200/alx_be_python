# This script is a simple calculator that uses a match-case statement.
# Prompt the user to enter two numbers.
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter numbers only.")
    exit()
# Ask the user for the desired operation.
operation = input("Choose the operation (+, -, *, /): ")
result = None
# Use a match-case statement to perform the calculation.
match operation:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
    case _:
        print("Invalid operation. Please choose from +, -, *, or /.")

# Display the result if a valid operation was performed.
if result is not None:
    print(f"The result is {result}")