class Account:
    def __init__(self, client, balance):
        self.client = client
        self.balance = balance

    def get_client(self):
        return self.client

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount