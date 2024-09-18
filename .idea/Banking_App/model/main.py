import math
from Account import Account
from BankController import BankController

# Create a BankController instance and start the menu
if __name__ == "__main__":
    bank_controller = BankController()
    bank_controller.menu()

uj_account = Account.create_account()
uj_account.deposit(5)
print(uj_account.get_account_info())