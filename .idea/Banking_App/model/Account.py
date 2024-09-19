class Account:
    def __init__(self, first_name: str, last_name: str, pin_code: str, initial_balance: float = 0.0):
        self.first_name = first_name
        self.last_name = last_name
        self._pin_code = pin_code # pin code privat itt ugy lesz valami privat ha "_" kezdődik ha jol értem
        self.balance = max(0.0, initial_balance)  # nem mehet még negatívba de ezen valtoztathatnank
    
    def deposit(self, amount: float):
        #pénz számlára helyezése
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Amount must be greater than 0.")
    
    def withdraw(self,pin_code: str,amount: float):
        #pénz levétel a számláról
        if pin_code != self._pin_code:
            raise ValueError("Invalid pin code.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0.")
        
        self.balance -= amount
    
    def get_balance(self, pin_code: str):
        # vissza adja a jelenlegi összeget a számlán ha helyes a pin code
        if pin_code == self._pin_code:
            return self.balance
        else:
            raise ValueError("Invalid pin code.")
    
    def get_account_info(self):
        # visszad stringet ami tartalmazza a felhasznaló nevét és a számlán lévő összeget
        return f"Account Holder: {self.first_name} {self.last_name}\nBalance: ${self.balance:.2f}"
    

    @classmethod
    def create_account(cls):
        """felhasználói adatok bekérése"""
        first_name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")
        pin_code = input("Set a 4-digit pin code: ")
        
        # csakis 4 számjegy elfogadható pin kódként
        while len(pin_code) != 4 or not pin_code.isdigit():
            print("Pin code must be exactly 4 digits.")
            pin_code = input("Set a 4-digit pin code: ")

        try:
            initial_balance = float(input("Enter the initial balance: "))
        except ValueError:
            print("Invalid balance entered, setting balance to $0.")
            initial_balance = 0.0

        # Create an Account instance using cls (reference to the class)
        return cls(first_name=first_name, last_name=last_name, pin_code=pin_code, initial_balance=initial_balance)
    

    
