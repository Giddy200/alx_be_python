# bank_account.py

class BankAccount:
   

    def __init__(self, initial_balance=0.0):
        """
        Initializes the BankAccount with a starting balance.

        :param initial_balance: The starting balance of the account (default is 0.0).
        """
        # Encapsulated attribute
        self._account_balance = initial_balance

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance.

        :param amount: The amount to deposit.
        """
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Deducts the specified amount from the account balance if funds are sufficient.

        :param amount: The amount to withdraw.
        :return: True if the withdrawal was successful, False otherwise.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        if self._account_balance >= amount:
            self._account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self._account_balance:.2f}")

# End of bank_account.py