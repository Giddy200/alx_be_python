def perform_operation(num1, num2, operation: str):
    """Performs basic arithmetic operations on two numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform. Can be 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
        float: The result of the arithmetic operation.

    Raises:
        ValueError: If an unsupported operation is provided or if division by zero is attempted.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError(f"Unsupported operation: {operation}")
    from arithmetic_operations import perform_operation

def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()