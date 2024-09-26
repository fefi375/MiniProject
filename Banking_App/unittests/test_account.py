import unittest
from Banking_App.model.Account import Account

#Account 0 egyenleggel.
accountZero = Account("John", "Wick", "3456", 0.0)

accountOneThousand=Account("Nagy", "Helga", "3656", 1000)


class MyTestCase(unittest.TestCase):

    def test_balance(self):
        self.assertEqual(accountZero.get_balance(), 0.0)  # add assertion here
        self.assertEqual(accountOneThousand.get_balance(), 1000)
        self.assertEqual(accountOneThousand.get_balance()-1000, 0)


    

if __name__ == '__main__':
    unittest.main()
