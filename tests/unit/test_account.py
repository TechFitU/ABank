import unittest

from bank_app.account import Account


class AccountTest(unittest.TestCase):
    def setUp(self):
        self.account = Account('001', 50.0)

    def test_account_object_returns_current_balance(self):
        self.assertEqual(self.account.account_number, "001")
        self.assertEqual(self.account.balance, 50.0)

    def test_json(self):
        self.assertDictEqual({
            'account_number': '001',
            'balance': 50.0
        }, self.account.json())

    def test_account_representation(self):
        self.assertEqual(self.account.__repr__(),
                         "Account(id=001, balance=50.0)")

    def test_deposit_funds_with_right_amount(self):
        self.assertEqual(100.34, self.account.deposit_funds(50.34))
        self.assertEqual(150.68, self.account.deposit_funds('50.34'))

    def test_deposit_funds_with_wrong_amount_raises_exception(self):
        self.assertRaises(ValueError, self.account.deposit_funds, 'pepito')


if __name__ == '__main__':
    # Running Unittests
    unittest.main()

    # Running Your Doctests
    import doctest

    doctest.testmod()
