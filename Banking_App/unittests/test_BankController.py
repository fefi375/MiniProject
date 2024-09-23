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
        self.assertEqual(bank_controller.accounts, {}, "A fiókok listályának üresnek kell lennie amikor a JSON file üres")