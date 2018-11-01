import unittest

from mock import Mock

from bank_app.account import Account
from bank_app.bank import Bank
from bank_app.bank import DBConnectionError


class BankTest(unittest.TestCase):

    def setUp(self):
        self.bank = Bank('Randolph')

    def test_bank_is_initially_empty(self):
        self.assertEqual({}, self.bank.accounts)
        self.assertEqual(len(self.bank.accounts), 0)

    def test_bank_representation(self):
        self.assertEqual("Bank(name=Randolph, accounts=0)", self.bank.__repr__())
        self.bank.add_account(Account('001', 50.00))
        self.assertEqual("Bank(name=Randolph, accounts=1)", self.bank.__repr__())

    def test_add_account(self):
        account_1 = Account('001', 50.00)
        account_2 = Account('002', 100.00)
        self.bank.add_account(account_1)
        self.bank.add_account(account_2)
        self.assertEqual(2, len(self.bank.accounts))

    def test_get_account_given_its_number_from_database(self):
        account_data = {"account_number": "001", "balance": 50}
        mock_data_interface = Mock()
        mock_data_interface.get.return_value = account_data
        self.bank.di = mock_data_interface

        self.assertEqual(account_data, self.bank.get_account('001'))
        mock_data_interface.get.assert_called_once_with('001')

    def test_get_account_given_its_number(self):
        account_data = {"account_number": "001", "balance": 50}

        account_1 = Account('001', 50.00)
        self.bank.add_account(account_1)
        self.assertEqual(account_data, self.bank.get_account('001'))

    def test_get_account_catches_exception_raised_when_access_database(self):
        mock_data_interface = Mock()

        mock_data_interface.get.side_effect = DBConnectionError()
        self.bank.di = mock_data_interface
        self.assertEqual("Connection error occurred. Try Again.",
                         self.bank.get_account('001'))
        mock_data_interface.get.assert_called_once_with('001')

    def test_get_account_raises_exception_with_wrong_params(self):
        self.assertRaises(ValueError, self.bank.get_account, 50)

    def test_get_account_balance_given_its_number(self):
        account_1 = Account('001', 50.00)
        self.bank.add_account(account_1)
        self.assertEqual(50.00, self.bank.get_account_balance('001'))

    def test_get_account_balance_given_its_number_from_database(self):
        account_data = {"account_number": "001", "balance": 50.00}
        mock_data_interface = Mock()
        mock_data_interface.get.return_value = account_data
        self.bank.di = mock_data_interface

        self.assertEqual(50.00, self.bank.get_account_balance('001'))
        mock_data_interface.get.assert_called_once_with('001')

    def test_get_account_balance_catches_exception_raised_when_access_database(self):
        mock_data_interface = Mock()

        mock_data_interface.get.side_effect = DBConnectionError()
        self.bank.di = mock_data_interface
        self.assertEqual("Connection error occurred. Try Again.",
                         self.bank.get_account_balance('001'))
        mock_data_interface.get.assert_called_once_with('001')

    def test_get_account_balance_raises_exception_with_wrong_params(self):
        self.assertRaises(ValueError, self.bank.get_account_balance, 1)


if __name__ == '__main__':
    # Running Unittests
    unittest.main()
