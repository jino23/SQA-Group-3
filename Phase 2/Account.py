from User import User
class Account:
    def __init__(self, account_id, balance, account_name, user:User):
        self.account_id = account_id
        self.balance=balance
        self.account_name=account_name
        self.user=user

    