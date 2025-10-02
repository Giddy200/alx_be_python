# shopping_list_manager.py

def main():
    # Start with an empty list
    shopping_list = []

    while True:
        print("\n" + "="*30)
        print("Shopping List Manager")
        print("="*30)
        print("1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Exit")
        print("="*30)

        # Get user input and strip whitespace
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            # --- Add Item ---
            item = input("Enter the item to add: ").strip()
            if item: # Ensure the item name isn't empty
                shopping_list.append(item)
                print(f"'{item}' has been added to the list.")
            else:
                print("Item name cannot be empty.")

        elif choice == '2':
            # --- Remove Item ---
            if not shopping_list:
                print(" The shopping list is already empty. Nothing to remove.")
                continue

            item_to_remove = input("Enter the item to remove: ").strip()

            if item_to_remove in shopping_list:
                # Use list.remove() to remove the first occurrence of the item
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' has been removed from the list.")
            else:
                # Item not found
                print(f" '{item_to_remove}' was not found in the list.")

        elif choice == '3':
            # --- View List ---
            print("\n--- Current Shopping List ---")
            if shopping_list:
                # Use enumerate to display items with a number
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
            else:
                print("The list is empty! Time to go shopping. 🛍️")
            print("---------------------------\n")

        elif choice == '4':
            # --- Exit ---
            print("Thank you for using the Shopping List Manager. Goodbye!")
            break  # Exit the while loop

        else:
            # --- Invalid Choice ---
            print("Invalid choice. Please enter a number between 1 and 4.")

# Standard boilerplate to run the main function
if __name__ == "__main__":
    main()