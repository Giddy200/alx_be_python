# A script that draws a text-based square pattern of asterisks.
# Prompt the user to enter a positive integer for the size.
while True:
    try:
        size = int(input("Enter the size of the pattern: "))
        if size > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")
# Use nested loops to draw the square pattern.
row_count = 0
while row_count < size:
    # The inner loop handles the columns (asterisks) for each row.
    for _ in range(size):
        print("*", end="")
    # Print a newline character after each row is complete.
    print()
    # Increment the row counter for the while loop.
    row_count += 1