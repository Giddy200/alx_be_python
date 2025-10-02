# Objective: Illustrate variable scope using global conversion factors.

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius using the global factor.

    The formula is: Celsius = (Fahrenheit - 32) * (5/9)
    """
    # Accessing the global variable (read-only access is implicit)
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit using the global factor.

    The formula is: Fahrenheit = (Celsius * 9/5) + 32
    """
    # Accessing the global variable (read-only access is implicit)
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    """
    Handles user interaction, input validation, and performs the conversion.
    """
    print("--- Temperature Conversion Tool ---")
    
    # --- 1. Input Temperature Value with Validation ---
    while True:
        try:
            temp_input = input("Enter the temperature to convert: ")
            temperature = float(temp_input)
            break
        except ValueError:
            # Raise an error for non-numeric input as specified
            raise ValueError("Invalid temperature. Please enter a numeric value.")
    
    # --- 2. Input Unit and Perform Conversion ---
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    result_temp = None
    original_unit_str = ""
    converted_unit_str = ""

    if unit == 'F':
        # Convert F to C
        result_temp = convert_to_celsius(temperature)
        original_unit_str = "F"
        converted_unit_str = "C"
    elif unit == 'C':
        # Convert C to F
        result_temp = convert_to_fahrenheit(temperature)
        original_unit_str = "C"
        converted_unit_str = "F"
    else:
        print("Invalid unit input. Please enter 'C' or 'F'.")
        return # Exit the function if unit is invalid

    # --- 3. Display Result ---
    if result_temp is not None:
        print(f"\n{temperature}°{original_unit_str} is {result_temp}°{converted_unit_str}")
        print("-" * 35)

if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        # Catch and display the specific ValueError raised by main()
        print(f"\nERROR: {e}")