from Account import Account
from Account import User
import random


class Transaction:
    """Class to handle various banking transactions for both standard and admin users."""
    
    def __init__(self, account: Account):
        """
        Initialize a Transaction with the given account.
        
        :param account: An instance of Account representing the user's account.
        """
        self.account = account

    def login(self):
        """
        Prompt the user to log in as either a Standard or Admin user.
        Validates the account number (and name for Admin) before proceeding.
        """
        user_type = input("Enter (S) for Standard user or (A) for Admin user: ")

        if user_type == "S":
            # Standard user login
            print("Welcome Standard User \n")
            user_account = input("Enter account number: ")

            # Validate account number for standard user
            if user_account != self.account.account_id:
                print("Invalid account number.")
                print("Exiting....")
                return
            # Ensure that the account is not an admin account
            if self.account.user.Admin is True:
                print("ERROR - This is an Admin Account - Must Click Admin")
                print("Exiting....")
                return

            print("Successfully logged in!\n")
            self.options_for_standard()

        elif user_type == "A":
            # Admin user login
            print("Welcome Admin User \n")
            user_account = input("Enter account number: ")

            # Validate admin account number
            if user_account != self.account.account_id:
                print("Invalid account number.")
                print("Exiting....")
                return

            # Ensure that the account is marked as admin
            if self.account.user.Admin is not True:
                print("This is not an admin account.")
                print("Exiting....")
                return

            user_name = input("Enter account Name: ")

            # Validate admin account name
            if user_name != self.account.account_name:
                print("Invalid account name.")
                print("Exiting....")
                return

            print("Successfully logged in\n")
            self.options_for_Admin()

    def withdraw(self):
        """
        Handle the withdrawal transaction.
        Different flow is provided for standard and admin users.
        """
        if not self.account.user.Admin:
            # Standard user withdrawal
            print("Standard mode - Withdrawal")
            try:
                amount = float(input("Enter amount to withdraw (Max limit is $500 for standard users): "))
            except ValueError:
                print("ERROR: Please enter a valid numeric value.")
                print("Exiting....")
                return

            # Check maximum withdrawal limit for standard users
            if amount > 500:
                print("ERROR: Max withdrawal limit is $500 for standard users.")
                print("Exiting....")
                return

            # Check for sufficient funds
            if self.account.balance - amount < 0:
                print(f"ERROR: Insufficient funds to withdraw. Current Balance: {self.account.balance}.")
                print("Exiting....")
                return

            # Deduct the withdrawal amount from the account balance
            self.account.balance -= amount
            print(f"Withdrawal successful! New balance: {self.account.balance}")

        else:
            # Admin withdrawal flow (using a placeholder account for demonstration)
            user2 = User(False)
            account2 = Account("A12", 5, "K", user2, "NP", "A")

            print("Admin mode - Withdrawal")
            user_number = input("Enter Account Number: ")

            # Validate the account number for admin withdrawal
            if user_number != account2.account_id:
                print("ERROR: Account number invalid")
                print("Exiting....")
                return

            user_name = input("Enter Account Holder Name: ")

            # Validate the account holder name
            if user_name != account2.account_name:
                print("ERROR: Account Holder Name is invalid")
                print("Exiting....")
                return

            try:
                amount = float(input("Enter amount to withdraw: "))
            except ValueError:
                print("ERROR: Please enter a valid numeric value.")
                print("Exiting....")
                return

            # Check maximum withdrawal limit
            if amount > 500:
                print("ERROR: Max withdrawal limit is $500 for user.")
                print("Exiting....")
                return

            # Check for sufficient funds in the placeholder account
            if account2.balance - amount < 0:
                print(f"ERROR: Insufficient funds to withdraw. Current Account Balance: {account2.balance}")
                print("Exiting....")
                return

            # Deduct amount from the placeholder account
            account2.balance -= amount
            print(f"Withdrawal successful! New balance: {account2.balance}")

    def transfer(self):
        """
        Handle funds transfer between accounts.
        Provides separate flows for standard and admin users.
        """
        if not self.account.user.Admin:
            # Standard user transfer flow
            print("Standard mode - Transfer")
            from_account = input("Enter your account number: ")

            # Validate the source account number
            if from_account != self.account.account_id:
                print("ERROR: Invalid account number.")
                print("Exiting....")
                return

            to_account = input("Enter the account number to transfer to: ")

            # Ensure the recipient account is not the same as the sender's
            if to_account == self.account.account_id:
                print("ERROR: Cannot transfer to the same account.")
                print("Exiting....")
                return

            try:
                amount = float(input("Enter amount to transfer (Max limit is $1000 for standard users): "))
            except ValueError:
                print("ERROR: Invalid input. Please enter a numeric value.")
                print("Exiting....")
                return

            # Check maximum transfer limit for standard users
            if amount > 1000:
                print("ERROR: Maximum transfer limit is $1000 for standard users.")
                print("Exiting....")
                return

            # Check for sufficient funds
            if self.account.balance - amount < 0:
                print(f"ERROR: Insufficient funds. Current Balance: ${self.account.balance}.")
                print("Exiting....")
                return

            # Create a placeholder receiving account for demonstration purposes
            receiving_account = Account(to_account, 500, "Receiver", User(False), "NP", "A")

            # Perform the transfer by deducting and adding the funds
            self.account.balance -= amount
            receiving_account.balance += amount

            print("Transfer successful!")
            print(f"Your new balance: ${self.account.balance}")
            print(f"Receiving account ({to_account}) new balance: ${receiving_account.balance}")

        else:
            # Admin transfer flow
            print("Admin mode - Transfer")
            admin_name = input("Enter Account Holder Name: ")

            # Validate the admin account holder name
            if admin_name != self.account.account_name:
                print("ERROR: Invalid Account Holder Name.")
                print("Exiting....")
                return

            from_account = input("Enter the source account number: ")

            # Validate the source account number
            if from_account != self.account.account_id:
                print("ERROR: Invalid source account number.")
                print("Exiting....")
                return

            to_account = input("Enter the destination account number: ")

            # Ensure that funds are not transferred to the same account
            if to_account == self.account.account_id:
                print("ERROR: Cannot transfer to the same account.")
                print("Exiting....")
                return

            try:
                amount = float(input("Enter amount to transfer: "))
            except ValueError:
                print("ERROR: Invalid input. Please enter a numeric value.")
                print("Exiting....")
                return

            # Check for sufficient funds
            if self.account.balance - amount < 0:
                print(f"ERROR: Insufficient funds. Current Balance: ${self.account.balance}.")
                print("Exiting....")
                return

            # Create a placeholder receiving account for demonstration purposes
            receiving_account = Account(to_account, 500, "Receiver", User(False), "NP", "A")

            # Perform the transfer
            self.account.balance -= amount
            receiving_account.balance += amount

            print("Transfer successful!")
            print(f"Source account ({from_account}) new balance: ${self.account.balance}")
            print(f"Destination account ({to_account}) new balance: ${receiving_account.balance}")

    def paybill(self):
        """
        Process bill payment from the user's account.
        Validates the account and company before processing the payment.
        """
        print("Paying bill...")

        if self.account.user.Admin:
            # For admin, verify the account holder's name first
            account_holder_name = input("Enter the account holder's name: ")
            if account_holder_name != self.account.account_name:
                print("ERROR: Invalid account holder name.")
                print("Exiting....")
                return

        account_number = input("Enter your account number: ")

        # Validate that the bill is paid from the correct account
        if account_number != self.account.account_id:
            print("ERROR: You can only pay bills from your own account.")
            print("Exiting....")
            return

        # Define valid companies for bill payment
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
            print("ERROR: Invalid company selected.")
            print("Exiting....")
            return

        company_name = valid_companies[company_code]

        try:
            amount = float(input("Enter the amount to pay: "))
        except ValueError:
            print("ERROR: Invalid amount entered.")
            print("Exiting....")
            return

        # Check maximum bill payment limit for standard users
        if not self.account.user.Admin and amount > 2000:
            print("ERROR: Maximum bill payment in standard mode is $2000.")
            print("Exiting....")
            return

        # Check for sufficient funds
        if self.account.balance - amount < 0:
            print(f"ERROR: Insufficient funds. Your current balance is ${self.account.balance}.")
            print("Exiting....")
            return

        # Deduct the bill amount from the account balance
        self.account.balance -= amount

        print("Bill payment successful!")
        print(f"Paid ${amount} to {company_name}.")
        print(f"New balance: ${self.account.balance}")

    def deposit(self):
        """
        Deposit funds into the account.
        (Currently a placeholder function.)
        """
        print("Depositing funds...")

    def create(self):
        """
        Create a new account (Admin mode only).
        Validates input for name and balance before creating the account.
        """
        print("Create Account - Admin Mode\n")
        name = input("Enter name for account holder: ")

        # Validate that the name contains only letters
        if not name.replace(" ", "").isalpha():
            print("Invalid input. Name must contain only letters.")
            print("Exiting....")
            return

        # Validate name length
        if len(name) > 20:
            print("Invalid input. Name must not exceed 20 characters.")
            print("Exiting....")
            return

        try:
            balance_created = float(input("Enter amount for the balance: "))
        except ValueError:
            print("ERROR: Please enter a valid numeric value for balance.")
            print("Exiting....")
            return

        # Validate balance does not exceed allowed limit
        if balance_created >= 999999.99:
            print("Invalid input. Balance exceeds over $99,999.99")
            print("Exiting....")
            return

        # Generate a random 10-digit account number
        account_number = ''.join(str(random.randint(0, 9)) for _ in range(10))
        user_created = User(False)

        account_created = Account(account_number, balance_created, name, user_created, "NP", "A")

        # Display the created account details
        print("Account successfully Created\n")
        print(f"Account Number: {account_created.account_id}\n")
        print(f"Balance: {account_created.balance}\n")
        print(f"Account Name: {account_created.account_name}\n")
        print(f"Account Plan: {account_created.plan}\n")
        print(f"Activity: {account_created.activity}\n")

        self.options_after_create()

    def delete(self):
        """
        Delete an account (Admin mode only).
        Validates the account holder's name and number before deletion.
        """
        print("Deleting account...")

        if not self.account.user.Admin:
            print("ERROR: Only an admin can delete accounts.")
            print("Exiting....")
            return

        account_holder_name = input("Enter the account holder's name: ")

        # Validate that the account exists in the bank system
        if account_holder_name not in self.bank_system.accounts:
            print("ERROR: No account exists for this holder.")
            print("Exiting....")
            return

        account_number = input("Enter the account number: ")

        account = self.bank_system.accounts.get(account_holder_name)
        # Validate that the account number matches the account holder's account
        if account.account_id != account_number:
            print("ERROR: Account number does not match the holder's account.")
            print("Exiting....")
            return

        # Delete the account from the bank system
        del self.bank_system.accounts[account_holder_name]
        print(f"Account {account_number} for {account_holder_name} has been deleted successfully.")

        account.deleted = True

    def disable(self):
        """
        Disable an account.
        (Placeholder function for disabling an account.)
        """
        print("Disabling account...")

    def change_plan(self):
        """
        Change the payment plan of an account.
        Prompts for account validation and switches the plan from Student to Non-Student.
        """
        print("Change Plan")
        account_name = str()
        account_number = str()
        np = str()

        # Validate the account holder name using a placeholder standard account (account2)
        while account_name != account2.account_name:
            account_name = input("Enter Account Name to Be Changed: ")
            if account_name != account2.account_name:
                print("Invalid account name! Try again!")
            elif account_name == "":
                print("Please enter an account name!")

        # Validate the account number using a placeholder standard account (account2)
        while account_number != account2.account_id:
            account_number = input("Enter Account Number to Be Changed: ")
            if account_number != account2.account_id:
                print("This is not a valid account number!")
            elif account_number == "":
                print("Please enter an account number!")

        print("Account number validation successful")

        # Switch the payment plan from Student to Non-Student
        while np != "NP":
            np = input("Enter NP to switch the bank account payment plan from Student to Non-Student: ")
            if np == "":
                break
            elif np == "NP":
                account2.plan = "NP"
                print("Changed from student to non-student")
                print("All changes saved successfully. Returning to main menu...")
        self.options_for_Admin()

    def logout(self):
        """
        Log out of the current session.
        """
        print("logging out...")
        return

    def options_for_standard(self):
        """
        Display the menu options for standard users and process the selection.
        """
        print("--------------MENU SESSION----------------")
        code = input("01 - Withdrawal\n02 - Transfer\n03 - Pay Bill\n04 - Deposit\n00 - End of Session\nEnter the number: ")

        if code not in ["01", "02", "03", "04", "00"]:
            print("Error: invalid code.\n")
            print("Exiting....")
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
            print("Error: invalid code.\n")
            print("Exiting....")
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
        Display the menu options after creating an account.
        """
        print("--------------MENU SESSION----------------")
        code = input("00 - Logout:\nEnter the number: ")
        if code not in ["00"]:
            print("Error: invalid code.\n")
            print("Exiting....")
            return

        if code == "00":
            self.logout()


# Create an Admin account for demonstration purposes
user = User(True)
account = Account("A123", 500.0, "J", user, "NP", "A")

# Create a Standard account for demonstration purposes
user2 = User(False)
account2 = Account("S123", 500.0, "K", user2, "NP", "S")

# Initialize the Transaction with the admin account and start login process
transaction = Transaction(account)
transaction.login()
