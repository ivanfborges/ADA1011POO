from client import Client
from account import Account

client = Client("John Doe", "john.doe@example.com")
account = Account(client, 1000)

print(client.get_name())
print(client.get_email())
print(account.get_client())
print(account.get_balance())

account.deposit(500)
print(account.get_balance())

account.withdraw(200)
print(account.get_balance())