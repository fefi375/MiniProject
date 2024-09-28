import sqlite3

from Banking_App.model.Account import Account
import json
import os

class BankController:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.file_path=os.path.join(base_dir, 'database.db')
        self.setup_database()
        self.accounts = {} # szótárként való inicializálás miatt (biztonság kedvéért)
        self.accounts=self.load_accounts() # fiókok listalya
        self.logged_in_account = None  # bejelentkezett fiók



    def setup_database(self):
        connection=sqlite3.connect(self.file_path)
        cursor=connection.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS accounts (
        first_name TEXT,
        last_name TEXT,
        pin_code TEXT,
        balance REAL)"""
                       )
        connection.commit()
        connection.close()

    def load_accounts(self):
        #Adatbázis kapcsolat
        connection = sqlite3.connect(self.file_path)
        cursor = connection.cursor()

        # Lekérdezzük az összes accountot
        cursor.execute("SELECT first_name, last_name, pin_code, balance FROM accounts")
        accounts_data = cursor.fetchall()

        # Account objektumok visszakonvertálása
        accounts = {}
        for data in accounts_data:
            first_name, last_name, pin_code, balance = data
            account = Account(first_name, last_name, pin_code, balance)
            account_holder = f"{first_name} {last_name}"
            accounts[account_holder] = account

        connection.close()
        return accounts  # Üres szótárt ad vissza, ha nem létezik a fájl
      
    def save_accounts(self):
        """Elmenti az accountokat az SQLite3 adatbázisba."""
        connection = sqlite3.connect(self.file_path)
        cursor = connection.cursor()

        # Először töröljük a meglévő accountokat, majd újra beszúrjuk az összeset
        cursor.execute("DELETE FROM accounts")
        for account in self.accounts.values():
            cursor.execute('''
                INSERT INTO accounts (first_name, last_name, pin_code, balance)
                VALUES (?, ?, ?, ?)
            ''', (account.first_name.strip().lower(),
                  account.last_name.strip().lower(),
                  account._pin_code,
                  account.balance))

        connection.commit()
        connection.close()



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
        account_holder = input("Enter the account holder's name: ").strip().lower()
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
            self.save_accounts()
        

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
                print(f" deposited successfully.")
                self.save_accounts()
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