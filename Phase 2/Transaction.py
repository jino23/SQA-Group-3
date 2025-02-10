from Account import Account
from Account import User


    
class Transaction:


    def __init__(self, account: Account):
        self.account=account

    def login(self):
        userType= input("Enter (S) for Standard user or (A) for Admin user: ")
        if userType=="S":
            print("Welcome Standard User \n")
            userAccount= input("Enter account number: ")
            
            while userAccount!=self.account.account_id:
                print("Invalid account number. Please try again.")
                userAccount = input("Re Enter account number: ")
            print("Successfully logged in\n")
            self.options_for_standard()

        elif userType=="A":

            print("Welcome Admin User \n")
            userAccount= input("Enter account number: ")
            while userAccount != self.account.account_id:
                print("Invalid account number. Please try again.")
                userAccount = input("Re Enter account number: ")

            if self.account.user.Admin != True:
                    print("This is not an admin account exiting....")
                    return

           
            userName= input("Enter account Name: ")
            while userName!=self.account.account_name:
                print("Invalid account name. Please try again.")
                userName = input("Re Enter account Name: ")
            
            print("Successfully logged in\n")
            
            self.options_for_Admin()


    def options_for_standard(self):
        code=input("01 - Withdrawal\n02 - Transfer\n03 - Pay Bill\n04 - Deposit\n00 - End of Session\nEnter the number: ")
        
        while code not in ["01", "02", "03", "04", "00"]:
            print("Error invalid code enter again\n")
            code=input("01 - Withdrawal\n02 - Transfer\n03 - Pay Bill\n04 - Deposit\n00 - End of Session\nEnter the number: ")
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
        code=input("01 - Withdrawal\n02 - Transfer\n03 - Pay Bill\n04 - Deposit\n05 - Create\n06 - Delete\n07 - Disable\n08 - Change Plan\n00 - End of Session\nEnter the number: ")
        
        while code not in ["01","02","03","04","05","06","07","08","00"]:
            print("Error invalid code enter again\n")
            code=input("01 - Withdrawal\n02 - Transfer\n03 - Pay Bill\n04 - Deposit\n05 - Create\n06 - Delete\n07 - Disable\n08 - Change Plan\n00 - End of Session\nEnter the number: ")

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



    def withdraw(self):
        if not self.account.user.Admin:
            print("Standard  mode - Withdrawal")
            
            amount = float(input("Enter amount to withdraw (Max $500 for standard users): "))
            while amount > 500:
                print("ERROR: Max withdrawal limit is $500 for standard users.")
                amount = float(input("Enter amount to withdraw (Max $500 for standard users): "))
            while self.account.balance - amount < 0:
                print(f"ERROR: Insufficient funds to withdraw. Current Balance: {self.account.balance}")
                amount = float(input("Enter amount to withdraw (Max $500 for standard users): "))
            
            self.account.balance -= amount
            print(f"Withdrawal successful. New balance: {self.account.balance}")


        if self.account.user.Admin:

            user2 = User(False)  
            account2=Account("A12", 5, "K",user2)

            print("Admin mode - Withdrawal")

            UserNumber=(input("Enter account Number: "))
            while UserNumber!= account2.account_id:
                print("ERROR: Acount number invalid")
                UserNumber=(input("Enter account Number: "))

            UserName=(input("Enter Account Holder Name: "))
            while UserName!= account2.account_name:
                print("ERROR: Acount Holder Name is invalid ")
                UserNumber=(input("Enter Account Holder Name: "))

            
            amount = float(input("Enter amount to withdraw: "))
            while amount > 500:
                print("ERROR: Max withdrawal limit is $500 for user.")
                amount = float(input("Enter amount to withdraw (Max $500 for standard users): "))
            while account2.balance - amount < 0:
                print(f"ERROR: Insufficient funds to withdraw. Current Account Balance: {account2.balance} ")
                amount = float(input("Enter amount to withdraw (Max $500 for standard users): "))

            account2.balance=account2.balance-amount
            print(f"Withdrawal successful. New balance: {account2.balance}")






    def transfer(self):
        print("Performing transfer...")

    def paybill(self):
        print("Paying bill...")

    def deposit(self):
        print("Depositing funds...")

    def create(self):
        print("Creating account...")

    def delete(self):
        print("Deleting account...")

    def disable(self):
        print("Disabling account...")

    def change_plan(self):
        print("Changing account plan...")

    def logout(self):
        print("logout...")
            



            


        
user = User(True)  
account = Account("A123", 500.0, "J", user)  

user2 = User(False)  
account2=Account("A12", 5, "K",user2)



transaction = Transaction(account)


transaction.login()