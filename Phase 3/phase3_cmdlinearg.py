import sys
from Account import Account, User
import random

class Transaction:
    """
    Class to perform various banking transactions such as login, withdrawal,
    transfer, bill payment, deposit, account disabling, account creation,
    deletion, and changing account plans.
    """

    def __init__(self, account: Account):
        """
        Initialize a Transaction with a given account.
        :param account: An instance of Account representing the current account.
        """
        self.account = account

    def login(self):
        """
        Prompt the user to log in as either a Standard or Admin user.
        Validates the credentials before proceeding.
        """
        user_type = input("Enter (S) for Standard user or (A) for Admin user: ")

        if user_type == "S":
            # Standard user login
            print("Welcome Standard User\n")
            account_id = input("Enter account number: ")
            if account_id != self.account.account_id:
                print("Invalid account number.\nExiting....")
                return
            # Ensure that this is not an admin account
            if self.account.user.Admin is True:
                print("ERROR - This is an Admin Account - Must Click Admin.\nExiting....")
                return

            print("Successfully logged in!\n")
            self.options_for_standard()

        elif user_type == "A":
            # Admin user login (modified order: account number first, then account name)
            print("Welcome Admin User\n")
            account_id = input("Enter account number: ")
            if account_id != self.account.account_id:
                print("Invalid account number.\nExiting....")
                return
            account_name = input("Enter account Name: ")
            if account_name != self.account.account_name:
                print("Invalid account name.\nExiting....")
                return
            if self.account.user.Admin is not True:
                print("This is not an admin account.\nExiting....")
                return

            print("Successfully logged in\n")
            self.options_for_Admin()
        else:
            print("Invalid user type selected.\nExiting....")
            return

    def withdraw(self):
        """
        Process a withdrawal transaction.
        Separate flows exist for standard and admin users.
        """
        if not self.account.user.Admin:
            # Standard user withdrawal flow
            print("Standard mode - Withdrawal")
            try:
                amount = float(input("Enter amount to withdraw (Max limit is $500 for standard users): "))
            except ValueError:
                print("ERROR: Please enter a valid number.\nExiting....")
                return

            if amount > 500:
                print("ERROR: Max withdrawal limit is $500 for standard users.\nExiting....")
                return

            if self.account.balance - amount < 0:
                print(f"ERROR: Insufficient funds. Current Balance: {self.account.balance}.\nExiting....")
                return

            self.account.balance -= amount
            print(f"Withdrawal successful! New balance: {self.account.balance}")
            self.options_for_standard()

        else:
            # Admin user withdrawal flow using a placeholder account
            placeholder_user = User(False)
            placeholder_account = Account("A12", 5, "K", placeholder_user, "NP", "A")
            print("Admin mode - Withdrawal")
            input_name = input("Enter Account Holder Name: ")
            if input_name != placeholder_account.account_name:
                print("ERROR: Account Holder Name is invalid.\nExiting....")
                return
            input_account = input("Enter Account Number: ")
            if input_account != placeholder_account.account_id:
                print("ERROR: Account number invalid.\nExiting....")
                return
            try:
                amount = float(input("Enter amount to withdraw: "))
            except ValueError:
                print("ERROR: Please enter a valid number.\nExiting....")
                return
            if amount > 500:
                print("ERROR: Max withdrawal limit is $500 for admin users.\nExiting....")
                return
            if placeholder_account.balance - amount < 0:
                print(f"ERROR: Insufficient funds. Current Account Balance: {placeholder_account.balance}.\nExiting....")
                return
            placeholder_account.balance -= amount
            print(f"Withdrawal successful! New balance: {placeholder_account.balance}")
            self.options_for_Admin()

    def transfer(self):
        """
        Process a transfer transaction.
        Implements separate flows for standard and admin users.
        """
        # Standard User Transfer Flow
        if not self.account.user.Admin:
            print("Standard mode - Transfer")
            from_account = input("Enter your account number: ")
            if from_account != self.account.account_id:
                print("ERROR: Invalid account number.\nExiting....")
                return
            to_account = input("Enter the account number to transfer to: ")
            if to_account == self.account.account_id:
                print("ERROR: Cannot transfer to the same account.\nExiting....")
                return
            try:
                amount = float(input("Enter amount to transfer (Max limit is $1000 for standard users): "))
            except ValueError:
                print("ERROR: Invalid input. Please enter a numeric value.\nExiting....")
                return
            if amount > 1000:
                print("ERROR: Maximum transfer limit is $1000 for standard users.\nExiting....")
                return
            if self.account.balance - amount < 0:
                print(f"ERROR: Insufficient funds. Current Balance: ${self.account.balance}.\nExiting....")
                return
            receiving_account = Account(to_account, 500, "Receiver", User(False), "NP", "A")
            self.account.balance -= amount
            receiving_account.balance += amount
            print("Transfer successful!")
            print(f"Your new balance: ${self.account.balance}")
            print(f"Receiving account ({to_account}) new balance: ${receiving_account.balance}")
            self.options_for_standard()

        else:
            # Admin Transfer Flow
            print("Admin mode - Transfer")
            placeholder_user = User(False)
            placeholder_account = Account("A12", 500, "K", placeholder_user, "NP", "A")
            placeholder_user_to_send = User(False)
            placeholder_account_to_send = Account("909", 500, "ppp", placeholder_user_to_send, "NP", "A")
            name = input("Enter Account Holder Name: ")
            if name != placeholder_account.account_name:
                print("ERROR: Invalid Account Holder Name.\nExiting....")
                return
            from_account = input("Enter the source account number: ")
            if from_account != placeholder_account.account_id:
                print("ERROR: Invalid source account number.\nExiting....")
                return
            to_account = input("Enter the destination account number: ")
            if to_account != placeholder_account_to_send.account_id:
                print("ERROR: This account does not exist.\nExiting....")
                return
            if to_account == from_account:
                print("ERROR: Cannot transfer to the same account\n Exiting...")
                return
            try:
                amount = float(input("Enter amount to transfer: "))
            except ValueError:
                print("ERROR: Invalid input. Please enter a numeric value.\nExiting....")
                return
            if placeholder_account.balance - amount < 0:
                print(f"ERROR: Insufficient funds. Current Balance: ${self.account.balance}.\nExiting....")
                return
            placeholder_account.balance -= amount
            placeholder_account_to_send.balance += amount
            print("Transfer successful!")
            print(f"Source account ({placeholder_account.account_id}) new balance: ${placeholder_account.balance}")
            print(f"Destination account ({placeholder_account_to_send.account_id}) new balance: ${placeholder_account_to_send.balance}\n")
            self.options_for_Admin()

    def paybill(self):
        """
        Process a bill payment transaction.
        Separate flows exist for standard and admin users.
        """
        print("Paying bill...")
        if not self.account.user.Admin:
            print("Standard Mode - Pay Bill")
            account_number = input("Enter your account number: ")
            if account_number != self.account.account_id:
                print("ERROR: Invalid account number.\nExiting....")
                return
            valid_companies = {
                "EC": "The Bright Light Electric Company",
                "CQ": "Credit Card Company Q",
                "FI": "Fast Internet, Inc."
            }
            print("Choose the company to pay:")
            for code, name in valid_companies.items():
                print(f"{code} - {name}")
            company_code = input("Enter company code (EC, CQ, FI): ").strip().upper()
            if company_code not in valid_companies:
                print("ERROR: Invalid company selected.\nExiting....")
                return
            company_name = valid_companies[company_code]
            try:
                amount = float(input("Enter the amount to pay (Max $2000 for standard users): "))
            except ValueError:
                print("ERROR: Invalid amount entered.\nExiting....")
                return
            if amount > 2000:
                print("ERROR: Maximum bill payment in standard mode is $2000.\nExiting....")
                return
            if self.account.balance - amount < 0:
                print(f"ERROR: Insufficient funds. Your current balance is ${self.account.balance}.\nExiting....")
                return
            self.account.balance -= amount
            print("Bill payment successful!")
            print(f"Paid ${amount} to {company_name}.")
            print(f"New balance: ${self.account.balance}\n")
            self.options_for_standard()

        else:
            print("Admin Mode - Pay Bill")
            placeholder_user = User(False)
            placeholder_account = Account("A12", 500, "K", placeholder_user, "NP", "A")
            input_name = input("Enter Account Holder Name: ")
            if input_name != placeholder_account.account_name:
                print("ERROR: Account Holder Name is invalid.\nExiting....")
                return
            input_account = input("Enter Account Number: ")
            if input_account != placeholder_account.account_id:
                print("ERROR: Account number invalid.\nExiting....")
                return
            valid_companies = {
                "EC": "The Bright Light Electric Company",
                "CQ": "Credit Card Company Q",
                "FI": "Fast Internet, Inc."
            }
            print("Choose the company to pay:")
            for code, name in valid_companies.items():
                print(f"{code} - {name}")
            print("Choose the company to pay:")
            for code, name in valid_companies.items():
                print(f"{code} - {name}")
            company_code = input("Enter company code (EC, CQ, FI): ").strip().upper()
            if company_code not in valid_companies:
                print("ERROR: Invalid company selected.\nExiting....")
                return
            company_name = valid_companies[company_code]
            try:
                amount = float(input("Enter the amount to pay (Max $5000 for admin users): "))
            except ValueError:
                print("ERROR: Invalid amount entered.\nExiting....")
                return
            if amount > 5000:
                print("ERROR: Maximum bill payment for admin mode is $5000.\nExiting....")
                return
            if placeholder_account.balance - amount < 0:
                print(f"ERROR: Insufficient funds. Current balance: ${placeholder_account.balance}.\nExiting....")
                return
            placeholder_account.balance -= amount
            print("Bill payment successful!")
            print(f"Paid ${amount} to {company_name}.")
            print(f"New balance: ${placeholder_account.balance}\n")
            self.options_for_Admin()

    def deposit(self):
        """
        Process a deposit transaction.
        Separate flows exist for standard and admin users.
        """
        if not self.account.user.Admin:
            print("Standard mode - Deposit")
            try:
                amount = float(input("Enter amount to deposit (Max $500 for standard users): "))
            except ValueError:
                print("ERROR: Please enter a valid number.\nExiting....")
                return
            if amount > 500:
                print("ERROR: Max deposit limit is $500 for standard users.\nExiting....")
                return
            self.account.balance += amount
            print(f"Deposit successful. New balance: {self.account.balance}")
            self.options_for_standard()

        else:
            admin_user = User(True)
            placeholder_account = Account("A123", 500.0, "J", admin_user, "NP", "A")
            print("Admin mode - Deposit")
            input_name = input("Enter Account Holder Name: ")
            if input_name != placeholder_account.account_name:
                print("ERROR: Account Holder Name is invalid.\nExiting....")
                return
            input_account = input("Enter account Number: ")
            if input_account != placeholder_account.account_id:
                print("ERROR: Account number invalid.\nExiting....")
                return
            try:
                amount = float(input("Enter amount to deposit: "))
            except ValueError:
                print("ERROR: Please enter a valid number.\nExiting....")
                return
            if amount > 500:
                print("ERROR: Max deposit limit is $500 for admin users.\nExiting....")
                return
            placeholder_account.balance += amount
            print(f"Deposit successful. New balance: {placeholder_account.balance}")
            self.options_for_Admin()

    def disable(self):
        """
        Enable or disable an account (Admin mode only).
        """
        if self.account.user.Admin:
            print("Admin mode - Disable")
            placeholder_user = User(False)
            placeholder_account = Account("A12", 500.0, "K", placeholder_user, "NP", "A")
            input_name = input("Enter Account Holder Name: ")
            if input_name != placeholder_account.account_name:
                print("ERROR: Account Holder Name is invalid.\nExiting....")
                return
            input_account = input("Enter account Number: ")
            if input_account != placeholder_account.account_id:
                print("ERROR: Account number invalid.\nExiting....")
                return
            disable_input = input("Enter (A) to activate the account | Enter (D) to disable the account: ").strip().upper()
            if disable_input == "A":
                if placeholder_account.activity == "A":
                    print("This account is already active.\nExiting....")
                elif placeholder_account.activity == "D":
                    placeholder_account.activity = "A"
                    print("Account successfully activated.\nExiting....")
            elif disable_input == "D":
                if placeholder_account.activity == "D":
                    print("This account is already disabled.\nExiting....")
                elif placeholder_account.activity == "A":
                    placeholder_account.activity = "D"
                    print("Account successfully disabled.\nExiting....")
            else:
                print("ERROR: Invalid activity type.\nExiting....")
                return
            self.options_for_Admin()

    def create(self):
        """
        Create a new account (Admin mode only).
        """
        print("Create Account - Admin Mode\n")
        name = input("Enter name for account holder: ")
        if not name.replace(" ", "").isalpha():
            print("Invalid input. Name must contain only letters.\nExiting....")
            return
        if len(name) > 20:
            print("Invalid input. Name must not exceed 20 characters.\nExiting....")
            return
        try:
            balance_created = float(input("Enter amount for the balance: "))
        except ValueError:
            print("ERROR: Please enter a valid number for balance.\nExiting....")
            return
        if balance_created >= 999999.99:
            print("Invalid input. Balance exceeds $99,999.99.\nExiting....")
            return
        account_number = ''.join(str(random.randint(0, 9)) for _ in range(10))
        user_created = User(False)
        account_created = Account(account_number, balance_created, name, user_created, "NP", "A")
        print("Account successfully created\n")
        print(f"Account Number: {account_created.account_id}")
        print(f"Balance: {account_created.balance}")
        print(f"Account Name: {account_created.account_name}")
        print(f"Account Plan: {account_created.plan}")
        print(f"Account Activity: {account_created.activity}\n")
        self.options_after_create()

    def delete(self):
        """
        Delete an account (Admin mode only).
        Note: This method assumes a 'bank_system' attribute exists with an 'accounts'
        dictionary.
        """
        print("Deleting account...")
        if not self.account.user.Admin:
            print("ERROR: Only an admin can delete accounts.\nExiting....")
            return
        account_holder_name = input("Enter the account holder's name: ")
        if account_holder_name not in self.bank_system.accounts:
            print("ERROR: No account exists for this holder.\nExiting....")
            return
        account_number = input("Enter the account number: ")
        account = self.bank_system.accounts.get(account_holder_name)
        if account.account_id != account_number:
            print("ERROR: Account number does not match the holder's account.\nExiting....")
            return
        del self.bank_system.accounts[account_holder_name]
        print(f"Account {account_number} for {account_holder_name} has been deleted successfully.")
        account.deleted = True
        self.options_for_Admin()

    def change_plan(self):
        """
        Change the payment plan of an account (Admin mode only).
        Allows switching between NP (Non-Student Plan) and SP (Student Plan).
        """
        if not self.account.user.Admin:
            print("ERROR: Only an Admin can change account plans.\nExiting....")
            return
        print("Admin Mode - Change Account Plan")
        placeholder_user = User(False)
        placeholder_account = Account("A12", 500.0, "K", placeholder_user, "NP", "A")
        input_name = input("Enter Account Holder Name: ")
        if input_name != placeholder_account.account_name:
            print("ERROR: Account Holder Name is invalid.\nExiting....")
            return
        input_account = input("Enter Account Number: ")
        if input_account != placeholder_account.account_id:
            print("ERROR: Account number invalid.\nExiting....")
            return
        print(f"Current Plan for {placeholder_account.account_name}: {placeholder_account.plan}")
        new_plan = input("Enter 'NP' to switch to Non-Student Plan or 'SP' to switch to Student Plan: ").strip().upper()
        if new_plan not in ["NP", "SP"]:
            print("ERROR: Invalid input. Please enter 'NP' or 'SP'.\nExiting....")
            return
        placeholder_account.plan = new_plan
        print(f"Plan successfully changed to {placeholder_account.plan} for account {placeholder_account.account_id}.")
        print("All changes saved successfully. Returning to main menu...")
        self.options_for_Admin()

    def logout(self):
        """
        Log out of the current session.
        """
        print("\n\nLogging out...")
        return

    def options_for_standard(self):
        """
        Display the menu options for standard users and process the selection.
        """
        print("--------------MENU SESSION----------------")
        code = input("01 - Withdrawal\n02 - Transfer\n03 - Pay Bill\n04 - Deposit\n00 - End of Session\nEnter the number: ")
        if code not in ["01", "02", "03", "04", "00"]:
            print("Error: Invalid code.\nExiting....")
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
        code = input("01 - Withdrawal\n02 - Transfer\n03 - Pay Bill\n04 - Deposit\n05 - Create\n06 - Delete\n07 - Disable\n08 - Change Plan\n00 - End of Session\nEnter the number: ")
        if code not in ["01", "02", "03", "04", "05", "06", "07", "08", "00"]:
            print("Error: Invalid code.\nExiting....")
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
        code = input("00 - Logout:\nEnter the number: ")
        if code not in ["00"]:
            print("Error: Invalid code.\nExiting....")
            return
        if code == "00":
            self.logout()


# ----------------------------------------------------------------------
# Create demonstration accounts for testing

# Admin account for demonstration
admin_user = User(True)
admin_account = Account("A123", 500.0, "J", admin_user, "NP", "A")

# Standard account for demonstration
standard_user = User(False)
standard_account = Account("S123", 500.0, "K", standard_user, "NP", "S")

# For command-line use, we now redirect standard input and output.
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python phase3_cmdlinearg.py <input_file> <output_file>")
        sys.exit(1)
    input_file, output_file = sys.argv[1], sys.argv[2]
    sys.stdin = open(input_file, 'r')
    sys.stdout = open(output_file, 'w')
    # Here, we choose the admin account for demonstration (change as needed)
    user = User(True)
    account = Account("1001234", 500.0, "John Cena", user, "NP", "A")
    transaction = Transaction(account)
    transaction.login()
