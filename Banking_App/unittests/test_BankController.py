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