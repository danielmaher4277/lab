class Account():
    def __init__(self, name: str):
        self.__account_name = name  # initializing private name variable

        self.__account_balance = 0.0  # initializing private account balance variable

    def deposit(self, amount: float):
        if amount > 0:
            self.__account_balance += amount  # adds to account balance if greater then 0
            return True  # Transaction successful
        else:
            return False  # Transaction unsuccessful

    def withdraw(self, amount: float):
        if (amount > 0) and (amount <= self.__account_balance):
            self.__account_balance -= amount  # Withdraws amount from account if not a negative number or greater then account balance.
            return True  # Transaction successful
        else:
            return False  # Transaction unsuccessful

    def get_balance(self):  # Returns final value of account balance
        return self.__account_balance

    def get_name(self):  # Returns initial name variable
        return self.__account_name
