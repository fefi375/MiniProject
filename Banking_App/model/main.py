import tkinter as tk
from Banking_App.controller.BankController import BankController
from Banking_App.view.BankAppGUI import BankingAppGUI


# Create a BankController instance and start the menu
#if __name__ == "__main__":
#    bank_controller = BankController()
#    bank_controller.main_menu()

# Running the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = BankingAppGUI(root)
    root.mainloop()