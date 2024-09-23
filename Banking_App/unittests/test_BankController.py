import unittest
from unittest.mock import patch, mock_open, MagicMock
import json
from Banking_App.model.Account import Account
from Banking_App.controller.BankController import BankController

class TestBankController(unittest.TestCase):
    
    @patch('builtins.open', new_callable=mock_open, read_data='[]')
    @patch('os.path.exists', return_value=True)
    def test_load_accounts_empty(self, mock_exists, mock_open_file):
        """Fiókok betöltésének a tesztje ugy hogy a JSON file üres."""
        bank_controller = BankController()
        self.assertEqual(bank_controller.accounts, {}, "Accounts list should be empty when the JSON file is empty")
    
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists', return_value=True)
    def test_load_accounts_with_data(self, mock_exists, mock_open_file):
        """Fiókok betöltésének a tesztje ugy hogy a JSON file tartalmaz adatokat."""
        accounts_data = [
            {"first_name": "John", "last_name": "Doe", "pin_code": "1234", "balance": 1000},
            {"first_name": "Jane", "last_name": "Smith", "pin_code": "5678", "balance": 500}
        ]
        mock_open_file.return_value.read.return_value = json.dumps(accounts_data)
   
   
        with patch('Banking_App.model.Account') as MockAccount:
            mock_account_instance = MagicMock()
            MockAccount.side_effect = lambda first_name, last_name, pin_code, balance: mock_account_instance
            bank_controller = BankController()
         # teszt arra hogy megfelelően betoltődtek-e a fiókok
        self.assertEqual(len(bank_controller.accounts), 2, "There should be 2 accounts loaded.")
        self.assertTrue("John Doe" in bank_controller.accounts, "John Doe's account should be loaded.")
        self.assertTrue("Jane Smith" in bank_controller.accounts, "Jane Smith's account should be loaded.")

    @patch('builtins.open', new_callable=mock_open)
    def test_save_accounts(self, mock_open_file):
        """Fiók mentése JSON-re teszt."""
        bank_controller = BankController()
        
        # manuálisan létrehozott fiók
        account = MagicMock()
        account.first_name = "John"
        account.last_name = "Doe"
        account._pin_code = "1234"
        account.balance = 1000
        bank_controller.accounts = {"John Doe": account}
        
        bank_controller.save_accounts()
        
        # meggyőződünk hogy megfelelő adat íródott a JSON fileba
        expected_data = [
            {
                'first_name': "John",
                'last_name': "Doe",
                'pin_code': "1234",
                'balance': 1000,
            }
        ]
        mock_open_file().write.assert_called_once_with(json.dumps(expected_data, indent=4))   


    @patch('builtins.input', side_effect=['John Doe', '1234'])
    @patch('Banking_App.model.Account')
    def test_login_successful(self, mock_account_class, mock_input):
        """Sikeres bejelentkezés tezstelése."""
        account = MagicMock()
        account._pin_code = "1234"
        bank_controller = BankController()
        bank_controller.accounts = {"John Doe": account}
        
        bank_controller.login()

        # megnézzük hogy jelenleg bejelentkeztetett fiók az aminek lennie kell
        self.assertEqual(bank_controller.logged_in_account, account, "Login should set the correct account.")

    @patch('builtins.input', side_effect=['John Doe', '0000'])
    @patch('Banking_App.model.Account')
    def test_login_wrong_pin(self, mock_account_class, mock_input):
        """Hibás pin eseten elbukás tesztelése."""
        account = MagicMock()
        account._pin_code = "1234"
        bank_controller = BankController()
        bank_controller.accounts = {"John Doe": account}
        
        with patch('builtins.print') as mock_print:
            bank_controller.login()

            # ellenőrizzük hogy felhasználó látja e a hiba üzenetet
            mock_print.assert_any_call("Incorrect pin code. Please try again.")
            self.assertIsNone(bank_controller.logged_in_account, "Login should fail and not set any account.")

    @patch('builtins.input', side_effect=['Jane Doe', '0000'])
    def test_login_account_not_found(self, mock_input):
        """Teszt arra az esetre ha a fiók nem található."""
        bank_controller = BankController()
        bank_controller.accounts = {"John Doe": MagicMock()}

        with patch('builtins.print') as mock_print:
            bank_controller.login()

            # ellenőrizzük hogy felhasználó látja e a hiba üzenetet
            mock_print.assert_any_call("Account not found.")
            self.assertIsNone(bank_controller.logged_in_account, "Login should fail when account is not found.")

    @patch('builtins.input', side_effect=['Jane', 'Doe'])
    @patch('Banking_App.model.Account.create_account')
    def test_create_account(self, mock_create_account, mock_input):
        """Új fiók létrehozás teszt."""
        mock_account_instance = MagicMock()
        mock_create_account.return_value = mock_account_instance
        mock_account_instance.first_name = 'Jane'
        mock_account_instance.last_name = 'Doe'

        bank_controller = BankController()
        with patch('builtins.print') as mock_print:
            bank_controller.create_account()

            # megvizsgáljuk hogy tényleg létrejött e a fiók
            account_holder = 'Jane Doe'
            self.assertTrue(account_holder in bank_controller.accounts, "New account should be added.")
            mock_print.assert_any_call(f"Account for {account_holder} created successfully.")

if __name__ == '__main__':
    unittest.main()      