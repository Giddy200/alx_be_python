# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Performs division robustly, handling ZeroDivisionError and ValueError 
    for non-numeric inputs.

    :param numerator: The numerator as a string (from command line).
    :param denominator: The denominator as a string (from command line).
    :return: A string containing the division result or an error message.
    """
    try:
        # 1. Attempt to convert input strings to floats
        num = float(numerator)
        den = float(denominator)

        # 2. Attempt to perform division
        result = num / den
        
        # 3. Return success message
        return f"The result of the division is {result}"

    except ValueError:
        # Catches errors if float() conversion fails (e.g., input is "ten")
        return "Error: Please enter numeric values only."

    except ZeroDivisionError:
        # Catches errors if division by zero occurs (den is 0.0)
        return "Error: Cannot divide by zero."

# End of robust_division_calculator.py