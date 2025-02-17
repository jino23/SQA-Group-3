from Account import Account
from Account import User
import random
    
class Transaction:
    def __init__(self, account: Account):
        self.account = account

    def login(self):
        userType = input("Enter (S) for Standard user or (A) for Admin user: ")
        
        if userType == "S":
            print("Welcome Standard User \n")
            userAccount = input("Enter account number: ")
            
            if userAccount != self.account.account_id:
                print("Invalid account number.")
                print("Exiting....")
                return
            if self.account.user.Admin == True:
                print("ERROR - This is an Admin Account - Must Click Admin")
                print("Exiting....")
                return
                
            print("Successfully logged in!\n")
            self.options_for_standard()

        elif userType == "A":
            print("Welcome Admin User \n")
            userAccount = input("Enter account number: ")

            if userName != self.account.account_name:
                print("Invalid account name.")
                print("Exiting....")
                return
            
            if not userAccount == self.account.account_id:
                print("Invalid account number.")
                print("Exiting....")
                return
                
            if self.account.user.Admin != True:
                    print("This is not an admin account.")
                    print("Exiting....")
                    return

            userName = input("Enter account Name: ")
            
            
            
            print("Successfully logged in\n")
            self.options_for_Admin()

    def withdraw(self):
        if not self.account.user.Admin:
            print("Standard  mode - Withdrawal")
            
            amount = float(input("Enter amount to withdraw (Max limit is $500 for standard users): "))
            if amount > 500:
                print("ERROR: Max withdrawal limit is $500 for standard users.")
                print("Exiting....")
                return
                
            if self.account.balance - amount < 0:
                print(f"ERROR: Insufficient funds to withdraw. Current Balance: {self.account.balance}.")
                print("Exiting....")
                return
                
            self.account.balance -= amount
            print(f"Withdrawal successful! New balance: {self.account.balance}")


        if self.account.user.Admin:
            user2 = User(False)  
            account2 = Account("A12", 5, "K", user2, "NP", "A")

            print("Admin mode - Withdrawal")

            UserName=(input("Enter Account Holder Name: "))
            if UserName!= account2.account_name:
                print("ERROR: Acount Holder Name is invalid ")
                print("Exiting....")
                return

            UserNumber = (input("Enter Account Number: "))
            if UserNumber != account2.account_id:
                print("ERROR: Acount number invalid")
                print("Exiting....")
                return

            
                
            amount = float(input("Enter amount to withdraw: "))
            if amount > 500:
                print("ERROR: Max withdrawal limit is $500 for user.")
                print("Exiting....")
                return
               
            if account2.balance - amount < 0:
                print(f"ERROR: Insufficient funds to withdraw. Current Account Balance: {account2.balance} ")
                print("Exiting....")
                return
            
            account2.balance = account2.balance-amount
            print(f"Withdrawal successful!  New balance: {account2.balance}")

    def transfer(self):
        print("Performing transfer...")
        
        if self.account.user.Admin:
            account_holder_name = input("Enter Account Holder Name:  ")
            if account_holder_name!= self.account.account_name:
                print("ERROR: Invalid Account Holder Name")
                print("Exiting...")
                return
            
        from_account_holder = input("Enter the account number to transfer from: ")
        
        if from_account_holder != self.account.account_id:
            print("ERROR: Invalud Account Number")
            print("Exiting...")
            return
        
        to_account_holder = input("Enter the account number to transfer to: ")
        
        if to_account_holder!= self.account.account_id:
            print("ERROR: Invalud Account Number")
            print("Exiting...")
            return
        
        # placeholder for account in back-end
        receiving_account = Account("A12", 500, "bh", User(False), "NP", "A")  
        
        try:
            amount = float(input("Enter the amount to transfer: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            print("Exiting...")
            return
    
        if not self.amount.user.Admin and amount > 1000: 
            print("ERROR: Maximum transfer limit in standard mode is $1000.")
            print("Exiting...")
            return
    
        if self.account.balance - amount < 0:
            print(f"ERROR: Insufficient funds. Your current balance is ${self.account.balance}.")
            print("Exiting....")
            return

        if receiving_account.balance + amount < 0:
            print("ERROR: Receiving account balance must be at least $0.00 after transfer.")
            print("Exiting....")
            return

        # Perform the transfer
        self.account.balance -= amount
        receiving_account.balance += amount

        print(f"Transfer successful! New balance: ${self.account.balance}")
        print(f"Receiving account ({to_account_holder}) New balance: ${receiving_account.balance}")

    def paybill(self):
        print("Paying bill...")

        if not self.account.user.Admin:
            print("Standard Mode - Pay Bill")

            account_number = input("Enter your account number: ")
            if account_number != self.account.account_id:
                print("ERROR: Invalid Account number.")
                print("Exiting....")
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
                print("ERROR: Invalid company selected.")
                print("Exiting....")
                return

            company_name = valid_companies[company_code]

            try:
                amount = float(input("Enter the amount to pay (Max $2000 for standard users): "))
            except ValueError:
                print("ERROR: Invalid amount entered.")
                print("Exiting....")
                return

            if amount > 2000:
                print("ERROR: Maximum bill payment in standard mode is $2000.")
                print("Exiting....")
                return

            if self.account.balance - amount < 0:
                print(f"ERROR: Insufficient funds. Your current balance is ${self.account.balance}.")
                print("Exiting....")
                return

            self.account.balance -= amount
            print(f"Bill payment successful!")
            print(f"Paid ${amount} to {company_name}.")
            print(f"New balance: ${self.account.balance}")

        if self.account.user.Admin:
            print("Admin Mode - Pay Bill")

            # Creating an account object inside the method, like in withdraw()
            user2 = User(False)  
            account2 = Account("A12", 500, "K", user2, "NP", "A")

            userName = input("Enter Account Holder Name: ")
            if userName != account2.account_name:
                print("ERROR: Account Holder Name is invalid.")
                print("Exiting....")
                return

            userNumber = input("Enter Account Number: ")
            if userNumber != account2.account_id:
                print("ERROR: Account number invalid.")
                print("Exiting....")
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
                print("ERROR: Invalid company selected.")
                print("Exiting....")
                return

            company_name = valid_companies[company_code]

            try:
                amount = float(input("Enter the amount to pay (Max $5000 for admin users): "))
            except ValueError:
                print("ERROR: Invalid amount entered.")
                print("Exiting....")
                return

            if amount > 5000:
                print("ERROR: Maximum bill payment for admin mode is $5000.")
                print("Exiting....")
                return

            if account2.balance - amount < 0:
                print(f"ERROR: Insufficient funds. Current balance: ${account2.balance}.")
                print("Exiting....")
                return

            account2.balance -= amount
            print(f"Bill payment successful!")
            print(f"Paid ${amount} to {company_name}.")
            print(f"New balance: ${account2.balance}")


    def deposit(self):
    
        if not self.account.user.Admin:
            print("Standard  mode - Deposit")
            
            amount = float(input("Enter amount to deposit (Max $500 for standard users): "))
            if amount > 500:
                print("ERROR: Max deposit limit is $500 for standard users.")
                print("Exiting....")
                return
                
            if self.account.balance + amount < 0:
                print(f"ERROR: Insufficient funds to deposit. Current Balance: {self.account.balance}.")
                print("Exiting....")
                return
                    
            self.account.balance += amount
            print(f"Deposit successful. New balance: {self.account.balance}")

        if self.account.user.Admin:

            user = User(True)  
            account2=Account("A123", 500.0, "J", user, "NP", "A")

            print("Admin mode - Deposit")

            UserName=(input("Enter Account Holder Name: "))
            if UserName!= account2.account_name:
                print("ERROR: Acount Holder Name is invalid ")
                print("Exiting....")
                return

            UserNumber=(input("Enter account Number: "))
            if UserNumber!= account2.account_id:
                print("ERROR: Acount number invalid")
                print("Exiting....")
                return

            
                

            
            amount = float(input("Enter amount to deposit: "))
            if amount > 500:
                print("ERROR: Max deposit limit is $500 for user.")
                print("Exiting....")
                return
               
            if account2.balance + amount < 0:
                print(f"ERROR: Insufficient funds to deposit. Current Account Balance: {account2.balance} ")
                print("Exiting....")
                return
            account2.balance = account2.balance + amount
            print(f"deposit successful. New balance: {account2.balance}")
      

    def disable(self):
            
        if self.account.user.Admin==True:
            print("Admin  mode - Disable")
            user2 = User(False)  
            account2=Account("A12", 500.0, "K",user2, "NP", "A")

            UserName=(input("Enter Account Holder Name: "))
            if UserName!= account2.account_name:
                print("ERROR: Acount Holder Name is invalid ")
                print("Exiting....")
                return
            
            UserNumber=(input("Enter account Number: "))
            if UserNumber!= account2.account_id:
                print("ERROR: Acount number invalid")
                print("Exiting....")
                return

        # Display disable options
            disableInput = input("Enter (A) to activate the account | Enter (D) to disable the account: ")
            if disableInput=="A":
                if account2.activity=="A":
                    print("This account is already active\nExiting...")
                elif account2.activity=="D":
                    account2.activity="A"
                    print("Account successfully Activated\n Exiting.... ")
            elif disableInput=="D":
                if account2.activity=="D":
                    print("This account is already Disabled\nExiting...")
                elif account2.activity=="A":
                    account2.activity="D"
                    print("Account successfully Disabled\n Exiting.... ")

            else:
                print("ERROR - Invalid this type of activity does not exist\nExiting...")
                return


    #Create out put
    def create(self):
        print("Create Account - Admin Mode\n")
        name = input("Enter name for account holder: ")

        if not name.replace(" ", "").isalpha():
            print("Invalid input. Name must contain only letters.")
            print("Exiting....")
            return
        
        if len(name) > 20:
            print("Invalid input. Name must not exceed 20 characters.")
            print("Exiting....")
            return
        
        balanceCreated = float(input("Enter amount for the balance: "))
        if balanceCreated >= 999999.99:
            print("Invalid input. Balance exceeds over $99,999.99")
            print("Exiting....")
            return
        
        account_number = ''.join(str(random.randint(0, 9)) for _ in range(10))

        userCreated = User(False)

        accountCreated = Account(account_number,balanceCreated, name,userCreated,"NP", "A")

        print("Account successfully Created\n")
        print(f"Account Number: {accountCreated.account_id}\n")
        print(f"Balance: {accountCreated.balance}\n")
        print(f"Account Name: {accountCreated.account_name}\n")
        print(f"Account Plan: {accountCreated.plan}\n")
        print(f"Account Number: {accountCreated.activity}\n")
        
        self.options_after_create()
        
    def delete(self):
        print("Deleting account...")
        
        if not self.account.user.Admin:
            print("ERROR: Only an admin can delete accounts.")
            print("Exiting....")
            return

        account_holder_name = input("Enter the account holder's name: ")

        if account_holder_name not in self.bank_system.accounts:
            print("ERROR: No account exists for this holder.")
            print("Exiting....")
            return

        account_number = input("Enter the account number: ")

        account = self.bank_system.accounts.get(account_holder_name)
        if account.account_id != account_number:
            print("ERROR: Account number does not match the holder's account.")
            print("Exiting....")
            return

        del self.bank_system.accounts[account_holder_name]
        print(f"Account {account_number} for {account_holder_name} has been deleted successfully.")

        account.deleted = True
        
  

    def change_plan(self):
        if not self.account.user.Admin:
            print("ERROR: Only an Admin can change account plans.")
            print("Exiting....")
            return

        print("Admin Mode - Change Account Plan")

        # Creating a new account object inside the method (like in withdraw)
        user2 = User(False)  
        account2 = Account("A12", 500.0, "K", user2, "NP", "A")

        userName = input("Enter Account Holder Name: ")
        if userName != account2.account_name:
            print("ERROR: Account Holder Name is invalid.")
            print("Exiting....")
            return

        userNumber = input("Enter Account Number: ")
        if userNumber != account2.account_id:
            print("ERROR: Account number invalid.")
            print("Exiting....")
            return

        print(f"Current Plan for {account2.account_name}: {account2.plan}")
        
        # Allow Admin to change the plan to NP (Non-Student Plan) or SP (Student Plan)
        new_plan = input("Enter 'NP' to switch to Non-Student Plan or 'SP' to switch to Student Plan: ").strip().upper()

        if new_plan not in ["NP", "SP"]:
            print("ERROR: Invalid input. Please enter 'NP' or 'SP'.")
            print("Exiting....")
            return

        # Update the plan
        account2.plan = new_plan
        print(f"Plan successfully changed to {account2.plan} for account {account2.account_id}.")
        print("All changes saved successfully. Returning to main menu...")

        self.options_for_Admin()

            
    def logout(self):
        print("logging out...")
        return
            
    def options_for_standard(self):
        print("--------------MENU SESSION----------------")
        code=input("01 - Withdrawal\n02 - Transfer\n03 - Pay Bill\n04 - Deposit\n00 - End of Session\nEnter the number: ")
        
        if code not in ["01", "02", "03", "04", "00"]:
            print("Error invalid code.\n")
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
        print("--------------MENU SESSION----------------")
        code = input("01 - Withdrawal\n02 - Transfer\n03 - Pay Bill\n04 - Deposit\n05 - Create\n06 - Delete\n07 - Disable\n08 - Change Plan\n00 - End of Session\nEnter the number: ")
        
        if code not in ["01","02","03","04","05","06","07","08","00"]:
            print("Error invalid code. \n")
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
        elif code == "06" :
            self.delete()
        elif code == "07" :
            self.disable()
        elif code == "08":
            self.change_plan()
        elif code == "00":
            self.logout()


    def options_after_create(self):
        print("--------------MENU SESSION----------------")

        code = input("00 - Logout:\nEnter the number: ")
        if code not in ["00"]:
            print("Error invalid code.\n")
            print("Exiting....")
            return
        
        if code == 00:
            self.logout()
            
# this is an Admin account        
user = User(True)  
account = Account("A123", 500.0, "J", user, "NP", "A")  

# this is an Standard Account
user2 = User(False)  
account2 = Account("S123", 500.0, "K" ,user2, "NP", "S")

# transaction = Transaction(account)
transaction = Transaction(account)
transaction.login()
