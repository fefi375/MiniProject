import tkinter as tk
from tkinter import messagebox
from Banking_App.model.Account import Account
from Banking_App.controller.BankController import BankController

class BankingAppGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Banking App")
        self.master.geometry("400x300")  # Set fixed window size (width x height)
        self.master.resizable(False, False)  # Disable window resizing
        self.controller = BankController()

        self.main_menu()

    def main_menu(self):
        """Main menu screen"""
        self.clear_window()

        tk.Label(self.master, text="Welcome to the Banking App", font=("Arial", 16, "bold")).grid(row=0, column=1, pady=20)

        tk.Button(self.master, text="Log in", command=self.login_screen, width=15, height=2).grid(row=1, column=1, pady=10)
        tk.Button(self.master, text="Create Account", command=self.create_account_screen, width=15, height=2).grid(row=2, column=1, pady=10)

    def login_screen(self):
        """Login screen"""
        self.clear_window()

        tk.Label(self.master, text="Login", font=("Arial", 14)).grid(row=0, column=1, pady=20)

        tk.Label(self.master, text="Account Holder:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        tk.Label(self.master, text="Pin Code:").grid(row=2, column=0, padx=10, pady=5, sticky="e")

        self.account_entry = tk.Entry(self.master, width=25)
        self.account_entry.grid(row=1, column=1, pady=5)
        self.pin_entry = tk.Entry(self.master, show="*", width=25)
        self.pin_entry.grid(row=2, column=1, pady=5)

        tk.Button(self.master, text="Login", command=self.login, width=10).grid(row=3, column=1, pady=10)
        tk.Button(self.master, text="Back", command=self.main_menu, width=10).grid(row=4, column=1)

    def create_account_screen(self):
        """Account creation screen"""
        self.clear_window()

        tk.Label(self.master, text="Create Account", font=("Arial", 14)).grid(row=0, column=1, pady=20)

        tk.Label(self.master, text="First Name:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        tk.Label(self.master, text="Last Name:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        tk.Label(self.master, text="Pin Code:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        tk.Label(self.master, text="Initial Balance:").grid(row=4, column=0, padx=10, pady=5, sticky="e")

        self.first_name_entry = tk.Entry(self.master, width=25)
        self.first_name_entry.grid(row=1, column=1, pady=5)
        self.last_name_entry = tk.Entry(self.master, width=25)
        self.last_name_entry.grid(row=2, column=1, pady=5)
        self.pin_entry_create = tk.Entry(self.master, width=25)
        self.pin_entry_create.grid(row=3, column=1, pady=5)
        self.balance_entry = tk.Entry(self.master, width=25)
        self.balance_entry.grid(row=4, column=1, pady=5)

        tk.Button(self.master, text="Create", command=self.create_account, width=10).grid(row=5, column=1, pady=10)
        tk.Button(self.master, text="Back", command=self.main_menu, width=10).grid(row=6, column=1)

    def banking_dashboard(self):
        """Dashboard after logging in"""
        self.clear_window()

        tk.Label(self.master, text=f"Welcome {self.controller.logged_in_account.first_name}!", font=("Arial", 14)).grid(row=0, column=1, pady=20)

        tk.Button(self.master, text="Deposit", command=self.deposit_screen, width=15, height=2).grid(row=1, column=1, pady=10)
        tk.Button(self.master, text="Withdraw", command=self.withdraw_screen, width=15, height=2).grid(row=2, column=1, pady=10)
        tk.Button(self.master, text="Check Balance", command=self.check_balance, width=15, height=2).grid(row=3, column=1, pady=10)
        tk.Button(self.master, text="Log Out", command=self.main_menu, width=15, height=2).grid(row=4, column=1, pady=10)

    def deposit_screen(self):
        """Deposit screen"""
        self.clear_window()

        tk.Label(self.master, text="Deposit Money", font=("Arial", 14)).grid(row=0, column=1, pady=20)
        tk.Label(self.master, text="Amount:").grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.deposit_entry = tk.Entry(self.master, width=25)
        self.deposit_entry.grid(row=1, column=1, pady=5)

        tk.Button(self.master, text="Deposit", command=self.deposit, width=10).grid(row=2, column=1, pady=10)
        tk.Button(self.master, text="Back", command=self.banking_dashboard, width=10).grid(row=3, column=1)

    def withdraw_screen(self):
        """Withdraw screen"""
        self.clear_window()

        tk.Label(self.master, text="Withdraw Money", font=("Arial", 14)).grid(row=0, column=1, pady=20)
        tk.Label(self.master, text="Amount:").grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.withdraw_entry = tk.Entry(self.master, width=25)
        self.withdraw_entry.grid(row=1, column=1, pady=5)

        tk.Button(self.master, text="Withdraw", command=self.withdraw, width=10).grid(row=2, column=1, pady=10)
        tk.Button(self.master, text="Back", command=self.banking_dashboard, width=10).grid(row=3, column=1)

    def check_balance(self):
        """Show balance"""
        balance = self.controller.logged_in_account.get_balance()
        messagebox.showinfo("Balance", f"Current balance: ${balance:.2f}")

    def clear_window(self):
        """Clear the current window"""
        for widget in self.master.winfo_children():
            widget.destroy()

    def login(self):
        """Handle login"""
        account_holder = self.account_entry.get()
        pin_code = self.pin_entry.get()

        if account_holder in self.controller.accounts and self.controller.accounts[account_holder]._pin_code == pin_code:
            self.controller.logged_in_account = self.controller.accounts[account_holder]
            self.banking_dashboard()
        else:
            messagebox.showerror("Error", "Invalid account or pin")

    def create_account(self):
        """Handle account creation"""
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        pin_code = self.pin_entry_create.get()
        balance = self.balance_entry.get()

        account_holder = f"{first_name} {last_name}"

        if account_holder in self.controller.accounts:
            messagebox.showerror("Error", "Account already exists")
        else:
            try:
                balance = float(balance)
                new_account = Account(first_name, last_name, pin_code, balance)
                self.controller.accounts[account_holder] = new_account
                messagebox.showinfo("Success", f"Account for {account_holder} created successfully.")
                self.controller.save_accounts()
                self.controller.logged_in_account = new_account
                self.banking_dashboard()
            except ValueError:
                messagebox.showerror("Error", "Invalid balance amount")

    def deposit(self):
        """Handle deposit"""
        try:
            amount = float(self.deposit_entry.get())
            if amount > 0:
                self.controller.logged_in_account.deposit(amount)
                messagebox.showinfo("Success", f"Deposited ${amount:.2f}")
                self.banking_dashboard()
            else:
                messagebox.showerror("Error", "Amount must be positive")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")

    def withdraw(self):
        """Handle withdrawal"""
        try:
            amount = float(self.withdraw_entry.get())
            if amount > 0 and amount <= self.controller.logged_in_account.get_balance():
                self.controller.logged_in_account.withdraw(amount)
                messagebox.showinfo("Success", f"Withdrew ${amount:.2f}")
                self.banking_dashboard()
            else:
                messagebox.showerror("Error", "Invalid or insufficient amount")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")


# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    app = BankingAppGUI(root)
    root.mainloop()
