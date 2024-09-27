import unittest
from Banking_App.model.Account import Account

#Account 0 egyenleggel.
accountZero = Account("John", "Wick", "3456", 0.0)

accountOneThousand=Account("Nagy", "Helga", "3656", 1000)


class MyTestCase(unittest.TestCase):

    def test_balance(self):
        self.assertEqual(accountZero.get_balance(), 0.0)
        self.assertEqual(accountOneThousand.get_balance(), 1000)
        self.assertEqual(accountOneThousand.get_balance()-1000, 0)
        self.assertGreater(accountOneThousand.get_balance(), accountZero.get_balance())

    def test_withdraw(self):
        self.assertRaises(ValueError, accountZero.withdraw, 1000)
        self.assertRaises(ValueError, accountOneThousand.withdraw, 0)
        self.assertRaises(ValueError, accountOneThousand.withdraw, 10001)
        self.assertRaises(ValueError, accountOneThousand.withdraw, -10)


    def test_deposit(self):
        accountDeposit = Account("Deposit", "Test", "0001", 0.0)
        accountDeposit.deposit(10.0)
        self.assertEqual(accountDeposit.get_balance(), 10.0)
        self.assertRaises(ValueError, accountDeposit.deposit, 0)

if __name__ == '__main__':
    unittest.main()
