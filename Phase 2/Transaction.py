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
            
            if not userAccount == self.account.account_id:
                print("Invalid account number.")
                print("Exiting....")
                return
                
            if self.account.user.Admin != True:
                    print("This is not an admin account.")
                    print("Exiting....")
                    return

            userName = input("Enter account Name: ")
            
            if userName != self.account.account_name:
                print("Invalid account name.")
                print("Exiting....")
                return
            
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

            UserNumber = (input("Enter Account Number: "))
            if UserNumber != account2.account_id:
                print("ERROR: Acount number invalid")
                print("Exiting....")
                return

            UserName=(input("Enter Account Holder Name: "))
            if UserName!= account2.account_name:
                print("ERROR: Acount Holder Name is invalid ")
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
        receiving_account = Account(to_account_holder, 500, "Receiver", User(False), "NP", "A")  
        
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
        
        if self.account.user.Admin:
            account_holder_name = input("Enter the account holder's name: ")
            if account_holder_name != self.account.account_name:
                print("ERROR: Invalid account holder name.")
                print("Exiting....")
                return

        account_number = input("Enter your account number: ")

        if account_number != self.account.account_id:
            print("ERROR: You can only pay bills from your own account.")
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
            amount = float(input("Enter the amount to pay: "))
        except ValueError:
            print("ERROR: Invalid amount entered.")
            print("Exiting....")
            return

        if not self.account.user.Admin and amount > 2000:
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

    def deposit(self):

        userType= input("Enter (S) for Standard user or (A) for Admin user: ")
        if userType=="S":
            print("Welcome Standard User \n")
                
            print("Successfully logged in\n")
            # self.options_for_standard()

        elif userType=="A":

            print("Welcome Admin User \n")
           
            
            print("Successfully logged in\n")
            
            # self.options_for_Admin()
        
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

            UserNumber=(input("Enter account Number: "))
            if UserNumber!= account2.account_id:
                print("ERROR: Acount number invalid")
                print("Exiting....")
                return

            UserName=(input("Enter Account Holder Name: "))
            if UserName!= account2.account_name:
                print("ERROR: Acount Holder Name is invalid ")
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
            print("Disabling account...")
            userType= input("Enter (S) for Standard user or (A) for Admin user: ")
            if userType=="S":
                print("Welcome Standard User \n")

            elif userType=="A":
                print("Welcome Admin User \n")


            if not self.account.user.Admin:
                print("Standard  mode - Disable")
                user = User(True)  
                account2=Account("A123", 500.0, "J",user)

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

                print("The account " + account2.account_id + " has been disabled..." )

            if self.account.user.Admin:
                print("Admin  mode - Disable")
                user2 = User(False)  
                account2=Account("A12", 500.0, "K",user2)

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

                print("The account " + account2.account_id + " has been disabled..." )
            
            return
            


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
        print("Change Plan")
        account_name = str
        account_number = str
        np = str

        while not account_name == account2.account_name: 
            account_name = input("Enter Account Name to Be Changed: ")
            if not account_name == account2.account_name:
                print("Invalid account name! Try again!")
            elif account_name == "":
                print("Please enter an account name!")

        while not account_number == account2.account_id:
            account_number = input("Enter Account Number to Be Changed: ")
            if not account_number == account2.account_id:
                print("This is not a valid account number!")
            elif account_number == "":
                print("Please enter an account number!")
           
        print("Account number validation successful")
        while not np == "NP":
            np = input("Enter NP to switch the bank account payment plan from Student to Non-Student.")
            if np == "":
                break
            elif np == "NP":
                account2.plan = "NP"
                print("Changed from student to non-student")
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
transaction = Transaction(account2)
transaction.login()
