class Account():
    def __init__(self, name):
        self.__account_name = name

        self.__account_balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return True  # Transaction successful
        else:
            return False  # Transaction unsuccessful

    def withdraw(self, amount):
        if (amount > 0) and (amount <= self.__account_balance):
            self.__account_balance -= amount
            return True  # Transaction successful
        else:
            return False  # Transaction unsuccessful

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name



