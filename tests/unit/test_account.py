import unittest

from bank_app.account import Account


class AccountTest(unittest.TestCase):
    def setUp(self):
        self.account = Account('001', 50.0)

    def test_init_fails_wrong_account_number_data_type(self):
        self.assertRaises(TypeError, Account, 33, 50.0)

    def test_init_fails_wrong_account_balance_data_value_or_type(self):
        self.assertRaises(ValueError, Account, '001', 'pepito')
        self.assertRaises(TypeError, Account, '001', dict())

    def test_account_object_returns_current_balance(self):
        account = Account('001', 50.0)
        self.assertEqual(account.account_number, "001")
        self.assertEqual(account.balance, 50.0)

        account = Account('001', '50.0')
        self.assertEqual(account.account_number, "001")
        self.assertEqual(account.balance, 50.0)

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

    def test_deposit_funds_fails_with_wrong_amount_raises_exception(self):
        self.assertRaises(ValueError, self.account.deposit_funds, 'pepito')

    def test_withdraw_funds_with_right_amount(self):
        self.assertEqual(0.0, self.account.withdraw_funds(50.0))
        self.account.balance = 50.0
        self.assertEqual(30.0, self.account.withdraw_funds('20.0'))

    def test_withdraw_funds_fails_with_wrong_amount_raises_exception(self):
        self.assertRaises(ValueError, self.account.withdraw_funds, 'pepito')

    def test_withdraw_funds_raises_exception_with_maximum_allowed(self):
        self.assertRaises(ValueError, self.account.withdraw_funds, 601.0)

    def test_withdraw_funds_raises_exception_when_not_enough_funds(self):
        self.assertEqual(50.0, self.account.balance)
        self.assertRaises(ValueError, self.account.withdraw_funds, 600.0)


if __name__ == '__main__':
    # Running Unittests
    unittest.main()

    # Running Your Doctests
    import doctest

    doctest.testmod()
