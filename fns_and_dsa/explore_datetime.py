from datetime import datetime, timedelta

def display_current_datetime():
    """
    Obtains and displays the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    # Used the directly imported 'datetime' class
    current_date = datetime.now()
    
    # Format the datetime object into the specified string format
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"\nCurrent date and time: {formatted_datetime}")
    # The current_date variable holds the datetime object, but we print the formatted string
    # We keep the current_date variable as required by the prompt
    return current_date

def calculate_future_date(current_date):
    """
    Prompts the user for a number of days, calculates the future date, 
    and prints it in 'YYYY-MM-DD' format.
    """
    while True:
        try:
            # Prompt the user for the number of days to add
            days_to_add_str = input("Enter the number of days to add to the current date: ")
            
            # Check for non-numeric input before attempting conversion
            if not days_to_add_str.isdigit():
                print("Invalid input. Please enter a whole number.")
                continue

            days_to_add = int(days_to_add_str)
            
            # Used the directly imported 'timedelta' class
            time_delta = timedelta(days=days_to_add)
            
            # Calculate the future date by adding the timedelta to the current date
            future_date = current_date + time_delta
            
            # Format the date part of the future_date object
            formatted_future_date = future_date.strftime("%Y-%m-%d")
            
            print(f"Future date: {formatted_future_date}")
            # The future_date variable holds the datetime object as required by the prompt
            return future_date

        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

def main():
    """
    The main execution function that calls the date/time operations.
    """
    print("--- Date and Time Operations Script ---")
    
    # Part 1: Display current date and time and capture the datetime object
    current_datetime_object = display_current_datetime()
    
    # Part 2: Calculate a future date using the captured datetime object
    calculate_future_date(current_datetime_object)
    
    print("\nScript finished.")

if __name__ == "__main__":
    main()