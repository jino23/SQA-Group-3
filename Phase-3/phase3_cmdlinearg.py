from Account import Account, User
import random
import sys
import io

class Transaction:
    """
    Class to perform various banking transactions such as login, withdrawal,
    transfer, bill payment, deposit, account disabling, account creation,
    deletion, and changing account plans.
    """

    def __init__(self):
        """
        Initialize a Transaction with no account yet.
        """
        self.account = None
        # If needed, initialize other attributes (e.g., a dummy bank_system for delete)
        self.bank_system = type("BankSystem", (), {"accounts": {}})()

    def login(self):
        # Create account objects internally for login comparisons.
        admin_user = User(True)
        admin_account = Account("A123", 500.0, "John Cena", admin_user, "NP", "A")

        standard_user = User(False)
        standard_account = Account("S123", 500.0, "Kobi", standard_user, "NP", "S")

        user_type = input("Enter (S) for Standard user or (A) for Admin user: \n").upper()

        if user_type == "S":
            # Standard user login
            print("\nWelcome Standard User\n")
            account_id = input("Enter account number: \n")
            if account_id != standard_account.account_id:
                print("Invalid account number.\nExiting....\n")
                return
            # Ensure that this is not an admin account
            if standard_account.user.Admin is True:
                print("ERROR - This is an Admin Account - Must Click Admin.\nExiting....\n")
                return

            print("Successfully logged in!\n")
            self.account = standard_account  # Update the account for later use
            self.options_for_standard()

        elif user_type == "A":
            # Admin user login (flipped: first account number, then name)
            print("\nWelcome Admin User\n")
            account_id = input("Enter account number:\n")
            if account_id != admin_account.account_id:
                print("Invalid account number.\nExiting....\n")
                return
            account_name = input("Enter account name: ")
            if account_name != admin_account.account_name:
                print("Invalid account name.\nExiting....\n")
                return
            if admin_account.user.Admin is not True:
                print("This is not an admin account.\nExiting....\n")
                return

            print("Successfully logged in\n")
            self.account = admin_account  # Update the account for later use
            self.options_for_Admin()
        else:
            print("Invalid user type selected.\nExiting....\n")
            return

    def withdraw(self):
        """
        Process a withdrawal transaction.
        Separate flows exist for standard and admin users.
        """
        if not self.account.user.Admin:
            # Standard user withdrawal flow
            print("\nStandard mode - Withdrawal\n")
            try:
                amount = float(input("\nEnter amount to withdraw (Max limit is $500 for standard users):\n"))
            except ValueError:
                print("\nERROR: Please enter a valid number.\nExiting....\n")
                return

            if amount > 500:
                print("\nERROR: Max withdrawal limit is $500 for standard users.\nExiting....\n")
                return

            if self.account.balance - amount < 0:
                print(f"\nERROR: Insufficient funds. Current Balance: {self.account.balance}.\nExiting....\n")
                return

            self.account.balance -= amount
            print(f"\nWithdrawal successful! New balance: {self.account.balance}\n")
            self.options_for_standard()

        else:
            # Admin user withdrawal flow using a placeholder account (flipped order)
            placeholder_user = User(False)
            placeholder_account = Account("A12", 500, "Kobz", placeholder_user, "NP", "A")
            print("\nAdmin mode - Withdrawal")
            input_account = input("\nEnter Account Number: \n")
            if input_account != placeholder_account.account_id:
                print("\nERROR: Account number invalid.\nExiting....\n")
                return
            input_name = input("\nEnter Account Holder Name: ")
            if input_name != placeholder_account.account_name:
                print("\nERROR: Account Holder Name is invalid.\nExiting....\n")
                return

            try:
                amount = float(input("\nEnter amount to withdraw: \n"))
            except ValueError:
                print("\nERROR: Please enter a valid number.\nExiting....\n")
                return

            if amount > 500:
                print("\nERROR: Max withdrawal limit is $500 for admin users.\nExiting....\n")
                return

            if placeholder_account.balance - amount < 0:
                print(f"\nERROR: Insufficient funds. Current Account Balance: {placeholder_account.balance}.\nExiting....\n")
                return

            placeholder_account.balance -= amount
            print(f"\nWithdrawal successful! New balance: {placeholder_account.balance}\n")
            self.options_for_Admin()

    def transfer(self):
        """
        Process a transfer transaction.
        Implements separate flows for standard and admin users.
        """
        # Standard User Transfer Flow
        if not self.account.user.Admin:
            print("Standard mode - Transfer")
            receiving_account = Account("123", 500, "Receiver", User(False), "NP", "A")
            from_account = input("Enter your account number: \n")
            if from_account != self.account.account_id:
                print("ERROR: Invalid account number.\nExiting....\n")
                return

            to_account = input("Enter the account number to transfer to: \n")
            if to_account != receiving_account.account_id:
                print("ERROR: Not a valid acocunt.\nExiting....\n")
                return

            try:
                amount = float(input("Enter amount to transfer (Max limit is $1000 for standard users): \n"))
            except ValueError:
                print("ERROR: Invalid input. Please enter a numeric value.\nExiting....\n")
                return

            if amount > 1000:
                print("ERROR: Maximum transfer limit is $1000 for standard users.\nExiting....\n")
                return

            if self.account.balance - amount < 0:
                print(f"ERROR: Insufficient funds. Current Balance: ${self.account.balance}.\nExiting....\n")
                return

            
            self.account.balance -= amount
            receiving_account.balance += amount

            print("Transfer successful!\n")
            print(f"Your new balance: ${self.account.balance}\n")
            print(f"Money Sent to Receiving account ({to_account})\n")
            self.options_for_standard()

        else:
            # Admin Transfer Flow (flipped order for source credentials)
            print("Admin mode - Transfer")
            # Use the logged-in admin account as the source account
            placeholder_account = Account("A1234", 500, "Kobzz", User(False), "NP", "A")
            # Create a destination placeholder account (separate from admin's account)
            placeholder_account_to_send = Account("S12", 500, "K", User(False), "NP", "A")

            from_account = input("Enter the source account number:\n")
            if from_account != placeholder_account.account_id:
                print("ERROR: Invalid source account number.\nExiting....\n")
                return
            name = input("Enter Account Holder Name for the source account: \n")
            if name != placeholder_account.account_name:
                print("ERROR: Invalid Account Holder Name.\nExiting....\n")
                return

            to_account = input("Enter the destination account number:\n")
            if to_account == placeholder_account.account_id:
                print("ERROR: Cannot transfer to the same account.\nExiting....\n")
                return
            if to_account != placeholder_account_to_send.account_id:
                print("ERROR: This account does not exist.\nExiting....\n")
                return
            
            amount = float(input("Enter amount to transfer:\n"))
            if placeholder_account.balance - amount < 0:
                print(f"ERROR: Insufficient funds. Current Balance: ${placeholder_account.balance}.\nExiting....\n")
                return

            placeholder_account.balance -= amount
            placeholder_account_to_send.balance += amount

            print("Transfer successful!\n")
            print(f"Source account ({placeholder_account.account_id}) new balance: ${placeholder_account.balance}\n")
            print(f"Destination account ({placeholder_account_to_send.account_id}) new balance: ${placeholder_account_to_send.balance}\n")
            self.options_for_Admin()

    def paybill(self):
        """
        Process a bill payment transaction.
        Separate flows exist for standard and admin users.
        """
        if not self.account.user.Admin:
            print("Standard Mode - Pay Bill\n")
            account_number = input("Enter your account number: \n")
            if account_number != self.account.account_id:
                print("\nERROR: Invalid account number.\nExiting....\n")
                return

            valid_companies = {
                "EC": "The Bright Light Electric Company",
                "CQ": "Credit Card Company Q",
                "FI": "Fast Internet, Inc."
            }

            print("\nChoose the company to pay:\n")
            for code, name in valid_companies.items():
                print(f"{code} - {name}")

            company_code = input("\nEnter company code (EC, CQ, FI): ").upper()
            if company_code not in valid_companies:
                print("ERROR: Invalid company selected.\nExiting....\n")
                return

            company_name = valid_companies[company_code]
            try:
                amount = float(input("\nEnter the amount to pay (Max $2000 for standard users): \n"))
            except ValueError:
                print("\nERROR: Invalid amount entered.\nExiting....\n")
                return

            if amount > 2000:
                print("\nERROR: Maximum bill payment in standard mode is $2000.\nExiting....\n")
                return

            if self.account.balance - amount < 0:
                print(f"\nERROR: Insufficient funds. Your current balance is ${self.account.balance}.\nExiting....\n")
                return

            self.account.balance -= amount
            print("\nBill payment successful!")
            print(f"\nPaid ${amount} to {company_name}.\n")
            print(f"\nNew balance: ${self.account.balance}\n")
            self.options_for_standard()

        else:
            # Admin Mode Pay Bill (flipped order)
            print("Admin Mode - Pay Bill")
            placeholder_user = User(False)
            placeholder_account = Account("A12", 500, "Kobz", placeholder_user, "NP", "A")
            input_account = input("Enter Account Number:\n")
            if input_account != placeholder_account.account_id:
                print("ERROR: Account number invalid.\nExiting....\n")
                return
            input_name = input("Enter Account Holder Name: ")
            if input_name != placeholder_account.account_name:
                print("ERROR: Account Holder Name is invalid.\nExiting....\n")
                return

            valid_companies = {
                "EC": "The Bright Light Electric Company",
                "CQ": "Credit Card Company Q",
                "FI": "Fast Internet, Inc."
            }

            print("Choose the company to pay:\n")
            for code, name in valid_companies.items():
                print(f"{code} - {name}")

            company_code = input("Enter company code (EC, CQ, FI): ").upper()
            if company_code not in valid_companies:
                print("ERROR: Invalid company selected.\nExiting....\n")
                return

            company_name = valid_companies[company_code]
            try:
                amount = float(input("Enter the amount to pay (Max $5000 for admin users): \n"))
            except ValueError:
                print("ERROR: Invalid amount entered.\nExiting....\n")
                return

            if amount > 5000:
                print("ERROR: Maximum bill payment for admin mode is $5000.\nExiting....\n")
                return

            if placeholder_account.balance - amount < 0:
                print(f"ERROR: Insufficient funds. Current balance: ${placeholder_account.balance}.\nExiting....\n")
                return

            placeholder_account.balance -= amount
            print("Bill payment successful!\n")
            print(f"Paid ${amount} to {company_name}.\n")
            print(f"New balance: ${placeholder_account.balance}\n")
            self.options_for_Admin()

    def deposit(self):
        """
        Process a deposit transaction.
        Separate flows exist for standard and admin users.
        """
        if not self.account.user.Admin:
            print("Standard mode - Deposit\n")
            try:
                amount = float(input("Enter amount to deposit (Max $500 for standard users): \n"))
            except ValueError:
                print("ERROR: Please enter a valid number.\nExiting....\n")
                return

            if amount > 500:
                print("ERROR: Max deposit limit is $500 for standard users.\nExiting....\n")
                return

            self.account.balance += amount
            print(f"Deposit successful. New balance: {self.account.balance}\n")
            self.options_for_standard()

        else:
            admin_user = User(False)
            placeholder_account = Account("S12", 500.0, "Kobz", admin_user, "NP", "A")

            print("Admin mode - Deposit")
            input_account = input("Enter account number:\n")
            if input_account != placeholder_account.account_id:
                print("ERROR: Account number invalid.\nExiting....\n")
                return
            input_name = input("Enter Account Holder Name:\n")
            if input_name != placeholder_account.account_name:
                print("ERROR: Account Holder Name is invalid.\nExiting....\n")
                return

            try:
                amount = float(input("Enter amount to deposit:\n"))
            except ValueError:
                print("ERROR: Please enter a valid number.\nExiting....\n")
                return

            if amount > 500:
                print("ERROR: Max deposit limit is $500 for admin users.\nExiting....\n")
                return

            placeholder_account.balance += amount
            print(f"Deposit successful. New balance: {placeholder_account.balance}\n")
            self.options_for_Admin()

    def disable(self):
        """
        Enable or disable an account (Admin mode only).
        """
        if self.account.user.Admin:
            print("Admin mode - Disable")
            placeholder_user = User(False)
            placeholder_account = Account("A12", 500.0, "Kobz", placeholder_user, "NP", "A")
            input_account = input("Enter account Number: ")
            if input_account != placeholder_account.account_id:
                print("ERROR: Account number invalid.\nExiting....\n")
                return
            input_name = input("Enter Account Holder Name: ")
            if input_name != placeholder_account.account_name:
                print("ERROR: Account Holder Name is invalid.\nExiting....\n")
                return

            disable_input = input("Enter (A) to activate the account | Enter (D) to disable the account:\n").upper()

            if disable_input == "A":
                if placeholder_account.activity == "A":
                    print("This account is already active.\nExiting....\n")
                elif placeholder_account.activity == "D":
                    placeholder_account.activity = "A"
                    print("Account successfully activated.\nExiting....\n")
            elif disable_input == "D":
                if placeholder_account.activity == "D":
                    print("This account is already disabled.\nExiting....\n")
                elif placeholder_account.activity == "A":
                    placeholder_account.activity = "D"
                    print("Account successfully disabled.\nExiting....\n")
            else:
                print("ERROR: Invalid activity type.\nExiting....\n")
                return
            self.options_for_Admin()

    def create(self):
        """
        Create a new account (Admin mode only).
        """
        print("Create Account - Admin Mode\n")
        name = input("Enter name for account holder: \n")

        if not name.replace(" ", "").isalpha():
            print("Invalid input. Name must contain only letters.\nExiting....\n")
            return

        if len(name) > 20:
            print("Invalid input. Name must not exceed 20 characters.\nExiting....\n")
            return

        try:
            balance_created = float(input("Enter amount for the balance: \n"))
        except ValueError:
            print("ERROR: Please enter a valid number for balance.\nExiting....\n")
            return

        if balance_created >= 99999.99:
            print("Invalid input. Balance exceeds $99,999.99.\nExiting....\n")
            return

        account_number = ''.join(str(random.randint(0, 9)) for _ in range(10))
        user_created = User(False)
        account_created = Account(account_number, balance_created, name, user_created, "NP", "A")

        print("Account successfully created\n")
        print(f"Account Number: {account_created.account_id}\n")
        print(f"Balance: {account_created.balance}\n")
        print(f"Account Name: {account_created.account_name}\n")
        print(f"Account Plan: {account_created.plan}\n")
        print(f"Account Activity: {account_created.activity}\n")
        self.options_after_create()

    def delete(self):
        """
        Delete an account (Admin mode only).
        Note: This method does NOT use self.bank_system.accounts.
        """
        if not self.account.user.Admin:
            print("ERROR: Only an admin can delete accounts.\nExiting....\n")
            return

        # Create a standard_account directly (same way login does)
        standard_user = User(False)
        standard_account = Account("S12", 500.0, "K", standard_user, "NP", "S")
        
        account_number = input("Enter the account number:\n")
        if account_number != standard_account.account_id:
            print("ERROR: Account number does not match the holder's account.\nExiting....\n")
            return

        account_holder_name = input("Enter the account holder's name:\n")
        if account_holder_name != standard_account.account_name:
            print("ERROR: No account exists for this holder.\nExiting....\n")
            return

        # Set deleted status instead of removing from self.bank_system
        standard_account.deleted = True
        print(f"Account {account_number} for {account_holder_name} has been deleted successfully.\n")
        self.options_for_Admin()

    def change_plan(self):
        """
        Change the payment plan of an account (Admin mode only).
        Allows switching between NP (Non-Student Plan) and SP (Student Plan).
        """
        if not self.account.user.Admin:
            print("ERROR: Only an Admin can change account plans.\nExiting....\n")
            return

        print("Admin Mode - Change Account Plan")
        placeholder_user = User(False)
        placeholder_account = Account("A12", 500.0, "Kobz", placeholder_user, "NP", "A")
        input_account = input("Enter Account Number: ")
        if input_account != placeholder_account.account_id:
            print("ERROR: Account number invalid.\nExiting....\n")
            return
        input_name = input("Enter Account Holder Name: \n")
        if input_name != placeholder_account.account_name:
            print("ERROR: Account Holder Name is invalid.\nExiting....\n")
            return

        print(f"Current Plan for {placeholder_account.account_name}: {placeholder_account.plan}")
        new_plan = input("Enter 'NP' to switch to Non-Student Plan or 'SP' to switch to Student Plan: \n").upper()

        if new_plan not in ["NP", "SP"]:
            print("ERROR: Invalid input. Please enter 'NP' or 'SP'.\nExiting....\n")
            return

        placeholder_account.plan = new_plan
        print(f"Plan successfully changed to {placeholder_account.plan} for account {placeholder_account.account_id}.")
        print("All changes saved successfully. Returning to main menu...\n")
        self.options_for_Admin()

    def logout(self):
        """
        Log out of the current session.
        """
        print("\n\nLogging out...\n")
        return

    def options_for_standard(self):
        """
        Display the menu options for standard users and process the selection.
        """
        print("--------------MENU SESSION----------------")
        code = input("01 - Withdrawal\n02 - Transfer\n03 - Pay Bill\n04 - Deposit\n00 - End of Session\nEnter the number: \n")
        if code == "":
            return  # If no further input, just stop here.
        if code not in ["01", "02", "03", "04", "00"]:
            print("Error: Invalid code.\nExiting....\n")
            return

        if code == "01":
            self.withdraw()
        elif code == "02":
            self.transfer()
        elif code == "03":
            self.paybill()
        elif code == "04":
            self.deposit()
        elif code == "00":
            self.logout()

    def options_for_Admin(self):
        """
        Display the menu options for admin users and process the selection.
        """
        print("--------------MENU SESSION----------------")
        code = input("01 - Withdrawal\n02 - Transfer\n03 - Pay Bill\n04 - Deposit\n05 - Create\n06 - Delete\n07 - Disable\n08 - Change Plan\n00 - End of Session\nEnter the number: \n")
        if code == "":
            return  # If no further input, just stop here.
        if code not in ["01", "02", "03", "04", "05", "06", "07", "08", "00"]:
            print("Error: Invalid code.\nExiting....\n")
            return

        if code == "01":
            self.withdraw()
        elif code == "02":
            self.transfer()
        elif code == "03":
            self.paybill()
        elif code == "04":
            self.deposit()
        elif code == "05":
            self.create()
        elif code == "06":
            self.delete()
        elif code == "07":
            self.disable()
        elif code == "08":
            self.change_plan()
        elif code == "00":
            self.logout()

    def options_after_create(self):
        """
        Display the menu options after account creation.
        """
        print("--------------MENU SESSION----------------")
        code = input("00 - Logout:\nEnter the number: \n")
        if code == "":
            return
        if code not in ["00"]:
            print("Error: Invalid code.\nExiting....\n")
            return
        if code == "00":
            self.logout()


# ----------------------------------------------------------------------
# Main block: if command-line arguments are provided, use them to simulate interactive input and capture output.
if __name__ == "__main__":
    if len(sys.argv) == 3:
        # Command-line mode: first argument is input file, second is output file.
        input_filename = sys.argv[1]
        output_filename = sys.argv[2]
        with open(input_filename, 'r') as f:
            input_lines = f.read().splitlines()
        input_iter = iter(input_lines)
        # Override input() so that it prints the prompt and then returns the next line.
        # If input_iter is exhausted, return an empty string.
        original_input = __builtins__.input
        __builtins__.input = lambda prompt="": (print(prompt, end=""), next(input_iter, ""))[1]
        # Capture printed output.
        original_stdout = sys.stdout
        sys.stdout = io.StringIO()
        transaction = Transaction()
        transaction.login()
        output_str = sys.stdout.getvalue()
        sys.stdout = original_stdout
        # Restore input() function.
        __builtins__.input = original_input
        with open(output_filename, 'w') as f:
            f.write(output_str)
    else:
        # Interactive mode
        transaction = Transaction()
        transaction.login()
