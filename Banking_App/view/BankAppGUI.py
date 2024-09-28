import tkinter as tk
from tkinter import messagebox
from Banking_App.model.Account import Account
from Banking_App.controller.BankController import BankController
import random
import os

class BankingAppGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Banking App")
        self.master.geometry("400x300")  # ablakméret
        self.master.resizable(False, False)  # nem lehet átméretezni
        self.controller = BankController()
        self.main_menu()
        self.master.config(background="#2eb774")

    def main_menu(self):
        """Fő menü"""
        self.clear_window()

        frame = tk.Frame(self.master)
        frame.place(relx=0.5, rely=0.5, anchor="center")  # középső frame

        tk.Label(frame, text="Welcome to the OI Banking App", font=("Verdana", 16, "bold"),bg='#38cb82').grid(row=0, column=0, columnspan=2, pady=20)

        tk.Button(frame, text="Log in", font=("Helvecita", 9, "bold"), command=self.login_screen, width=15, height=2).grid(columnspan=3, pady=10)
        tk.Button(frame, text="Create Account", font=("Helvecita", 9, "bold"), command=self.create_account_screen, width=15, height=2).grid(columnspan=3)
        frame.config(background="#38cb82")

    def login_screen(self):
        """Bejelentkezési menü"""
        self.clear_window()

        frame = tk.Frame(self.master)
        frame.place(relx=0.5, rely=0.5, anchor="center")  # középső frame
        frame.configure(background="#2eb774")

        tk.Label(frame, text="Login", font=("Verdana", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=20)

        tk.Label(frame, text="Account Holder:", font=("Helvecita", 10)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
        tk.Label(frame, text="Pin Code:", font=("Helvecita", 10)).grid(row=2, column=0, padx=10, pady=5, sticky="e")

        self.account_entry = tk.Entry(frame, width=25)
        self.account_entry.grid(row=1, column=1, pady=5)
        self.pin_entry = tk.Entry(frame, show="*", width=25)
        self.pin_entry.grid(row=2, column=1, pady=5)

        tk.Button(frame, text="Login", font=("Helvecita", 9),  command=self.login, width=10).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(frame, text="Back", font=("Helvecita", 9),  command=self.main_menu, width=10).grid(row=4, column=0, columnspan=2)

    def create_account_screen(self):
        """fiók létrehozási menü"""
        self.clear_window()

        frame = tk.Frame(self.master)
        frame.place(relx=0.5, rely=0.5, anchor="center")  # középső frame
        frame.configure(background="#2eb774")

        tk.Label(frame, text="Create Account",bg="#2eb774", font=("Verdana", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=20)

        tk.Label(frame, text="First Name:", font=("Helvecita", 10)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
        tk.Label(frame, text="Last Name:", font=("Helvecita", 10)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
        tk.Label(frame, text="Pin Code:", font=("Helvecita", 10)).grid(row=3, column=0, padx=10, pady=5, sticky="e")
        tk.Label(frame, text="Initial Balance:", font=("Helvecita", 10)).grid(row=4, column=0, padx=10, pady=5, sticky="e")

        self.first_name_entry = tk.Entry(frame, width=25)
        self.first_name_entry.grid(row=1, column=1, pady=5)
        self.last_name_entry = tk.Entry(frame, width=25)
        self.last_name_entry.grid(row=2, column=1, pady=5)
        self.pin_entry_create = tk.Entry(frame, width=25)
        self.pin_entry_create.grid(row=3, column=1, pady=5)
        self.balance_entry = tk.Entry(frame, width=25)
        self.balance_entry.grid(row=4, column=1, pady=5)

        tk.Button(frame, text="Create", font=("Helvecita", 9), command=self.create_account, width=10).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(frame, text="Back", font=("Helvecita", 9), command=self.main_menu, width=10).grid(row=6, column=0, columnspan=2)

    def banking_dashboard(self):
        """Bejelentkezés utáni menü"""
        self.clear_window()

        frame = tk.Frame(self.master)
        frame.place(relx=0.5, rely=0.5, anchor="center")  # középső frame
        frame.configure(background="#2eb774")
        tk.Label(frame,bg="#2eb774", text=f"Welcome {self.controller.logged_in_account.first_name} {self.controller.logged_in_account.last_name}!", font=("Verdana", 14, "bold")).grid(row=0, column=0, columnspan=3, pady=20)

        tk.Button(frame, text="Deposit", font=("Helvecita", 9), command=self.deposit_screen, width=15, height=2).grid(row=1, columnspan=3, pady=10)
        tk.Button(frame, text="Withdraw", font=("Helvecita", 9), command=self.withdraw_screen, width=15, height=2).grid(row=2, columnspan=3, pady=10)
        tk.Button(frame, text="Check Balance", font=("Helvecita", 9), command=self.check_balance, width=15, height=2).grid(row=3, columnspan=3, pady=10)
        tk.Button(frame, text="Log Out", font=("Helvecita", 9), command=self.main_menu, width=15, height=2).grid(row=4, columnspan=3, pady=10)

    def deposit_screen(self):
        """feltöltési menü"""
        self.clear_window()

        frame = tk.Frame(self.master)
        frame.place(relx=0.5, rely=0.5, anchor="center")  # középső frame

        tk.Label(frame, text="Deposit Money", font=("Verdana", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=20)
        tk.Label(frame, text="Amount:", font=("Helvecita", 10)).grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.deposit_entry = tk.Entry(frame, width=25)
        self.deposit_entry.grid(row=1, column=1, pady=5)

        tk.Button(frame, text="Deposit", font=("Helvecita", 9), command=self.deposit, width=10).grid(row=2, column=0, columnspan=3, pady=10)
        tk.Button(frame, text="Back", font=("Helvecita", 9), command=self.banking_dashboard, width=10).grid(row=3, column=0, columnspan=3)

    def withdraw_screen(self):
        """felvételi menü"""
        self.clear_window()

        frame = tk.Frame(self.master)
        frame.place(relx=0.5, rely=0.5, anchor="center")  # középső frame

        tk.Label(frame, text="Withdraw Money", font=("Verdana", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=20)
        tk.Label(frame, text="Amount:", font=("Helvecita", 10)).grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.withdraw_entry = tk.Entry(frame, width=25)
        self.withdraw_entry.grid(row=1, column=1, pady=5)

        tk.Button(frame, text="Withdraw", font=("Helvecita", 9), command=self.withdraw, width=10).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(frame, text="Back", font=("Helvecita", 9),  command=self.banking_dashboard, width=10).grid(row=3, column=0, columnspan=2)

    def check_balance(self):
        """összeg lekérdezés"""
        balance = self.controller.logged_in_account.get_balance()
        messagebox.showinfo("Balance", f"Current balance: ${balance:.2f}")

    def clear_window(self):
        """Ablaktörlő"""
        for widget in self.master.winfo_children():
            widget.destroy()

    def login(self):
        """Bejelentkezés kezelő"""
        account_holder = self.account_entry.get().strip().lower()
        pin_code = self.pin_entry.get()

        if account_holder in self.controller.accounts and self.controller.accounts[account_holder]._pin_code == pin_code:
            self.controller.logged_in_account = self.controller.accounts[account_holder]
            self.banking_dashboard()
        else:
            messagebox.showerror("Error", "Invalid account or pin")

    def create_account(self):
        """fiók létrehozást kezelő"""
        first_name = self.first_name_entry.get().strip().lower()
        last_name = self.last_name_entry.get().strip().lower()
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
        """Pénz feltöltő kezelő"""
        try:
            amount = float(self.deposit_entry.get())
            if amount > 0:
                self.controller.logged_in_account.deposit(amount)
                messagebox.showinfo("Success", f"Deposited ${amount:.2f}")
                self.controller.save_accounts()
                self.banking_dashboard()
            else:
                messagebox.showerror("Error", "Amount must be positive")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")

    def withdraw(self):
        """Pénz felvétel kezelő"""
        try:
            amount = float(self.withdraw_entry.get())
            if amount > 0 and amount <= self.controller.logged_in_account.get_balance():
                self.controller.logged_in_account.withdraw(amount)
                messagebox.showinfo("Success", f"Withdrew ${amount:.2f}")
                self.controller.save_accounts()
                self.banking_dashboard()
            else:
                messagebox.showerror("Error", "Invalid or insufficient amount")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")



