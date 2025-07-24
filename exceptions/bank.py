min_balance = 1000

class MinimumBalanceError(Exception):

    def __init__(self, message):
        super().__init__(message)

class Account:
    def __init__(self, amount):
        if amount < min_balance:
            raise MinimumBalanceError(f"Minimum Balance is {min_balance}")
        
        self.balance = amount
        print(f"Account opened successfull and balance is {self.balance}")

    def display_details(self):
        print(f"Account Balance is {self.balance}")