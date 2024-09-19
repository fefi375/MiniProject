from Banking_App.model.Account import Account
class BankController:
    def __init__(self):
        self.accounts = {}  # fiókok listalya
        self.logged_in_account = None  # bejelentkezett fiók

    def main_menu(self):
        """fő login menu"""
        while True:
            print("\n--- Welcome to the Banking System ---")
            print("1. Log in to an existing account")
            print("2. Create a new account")
            print("3. Exit")
            
            choice = input("Choose an option (1-3): ")
            
            if choice == '1':
                self.login()
            elif choice == '2':
                self.create_account()
            elif choice == '3':
                print("Exiting the banking system.")
                break
            else:
                print("Invalid option. Please choose a valid option.")

    def login(self):
        """bejelentkeztető"""
        account_holder = input("Enter the account holder's name: ")
        if account_holder in self.accounts:
            pin_code = input("Enter your 4-digit pin code: ")
            if pin_code == self.accounts[account_holder]._pin_code:
                print(f"Welcome, {account_holder}!")
                self.logged_in_account = self.accounts[account_holder]
                self.account_menu()  # Go to account menu after login
            else:
                print("Incorrect pin code. Please try again.")
        else:
            print("Account not found.")

    def create_account(self):
        """új fiók létrehozása."""
        account = Account.create_account()
        account_holder = account.first_name + " " + account.last_name
        
        if account_holder in self.accounts:
            print("An account with this name already exists.")
        else:
            self.accounts[account_holder] = account
            print(f"Account for {account_holder} created successfully.")
            self.logged_in_account = account
            self.account_menu()  # auto belépés miután kész az acc

    def account_menu(self):
        """bejelentkezés utáni menu"""
        while True:
            print("\n--- Account Menu ---")
            print(f"Logged in as: {self.logged_in_account.first_name} {self.logged_in_account.last_name}")
            print("1. Deposit money")
            print("2. Withdraw money")
            print("3. Check balance")
            print("4. Log out")
            
            choice = input("Choose an option (1-4): ")
            
            if choice == '1':
                self.logged_in_account.deposit(float(input("Enter the amount to deposit: ")))
                print(f" withdrawn successfully.")
            elif choice == '2':
                self.logged_in_account.withdraw(float(input("Enter the amount to withdraw: ")))
            elif choice == '3':
                balance = self.logged_in_account.get_balance()
                print(f"Current balance: ${balance:.2f}")
            elif choice == '4':
                print(f"Logging out {self.logged_in_account.first_name} {self.logged_in_account.last_name}.")
                self.logged_in_account = None
                break
            else:
                print("Invalid option. Please choose a valid option.")