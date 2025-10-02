def display_menu():
    """Prints the menu options for the shopping list manager."""
    # This line has been added/modified to strictly match the required string
    print("Shopping List Manager") 
    print("---------------------") # Adding a separator for neatness
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("---------------------\n")

def main():
    """
    Main function to run the shopping list manager loop.
    Initializes the shopping list and handles user input for list operations.
    """
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        # --- 1. Add Item ---
        if choice == '1':
            item_to_add = input("Enter the item to add: ").strip()
            if item_to_add: 
                shopping_list.append(item_to_add)
                print(f"'{item_to_add}' has been added to the list.")
            else:
                print("Item name cannot be empty.")
        
        # --- 2. Remove Item ---
        elif choice == '2':
            if not shopping_list:
                print("The list is currently empty. Nothing to remove.")
                continue 
            
            item_to_remove = input("Enter the item to remove: ").strip()
            
            try:
                # Attempt to find and remove the item
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' has been removed from the list.")
            except ValueError:
                # Catches the error if the item is not found in the list
                print(f"Error: '{item_to_remove}' was not found in the list.")

        # --- 3. View List ---
        elif choice == '3':
            print("\n*** YOUR SHOPPING LIST ***")
            if shopping_list:
                # Enumerate the list to display item numbers (1-based index)
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
            else:
                print("The list is empty. Time to go shopping!")
            print("**************************")
        
        # --- 4. Exit ---
        elif choice == '4':
            print("Thank you for using the Shopping List Manager. Goodbye! ")
            break
        
        # --- Invalid Choice ---
        else:
            print("Invalid choice. Please select an option from 1 to 4.")

if __name__ == "__main__":
    main()