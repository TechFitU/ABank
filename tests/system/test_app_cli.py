"""
Business requirements to test:
1. The customer must be able to uniquely access his bank account and retrieve the
balance.
2. The customer must be able to deposit funds (update account) into the bank account.
3. The customer must be able to withdraw funds from the bank account.
"""

import unittest

from mock import patch, call

from bank_app import app_cli
from bank_app.account import Account
from bank_app.bank import Bank


class AppCliTest(unittest.TestCase):
    def setUp(self):
        app_cli.current_bank = Bank("Randolph")
        app_cli.current_account = None

    def tearDown(self):
        del app_cli.current_bank
        del app_cli.current_account

    @staticmethod
    def test_menu_receives_empty_account_number_and_exits():
        with patch('builtins.print') as mocked_print:
            with patch('builtins.input', return_value="") as mocked_input:
                app_cli.menu()
                mocked_input.assert_called()
                mocked_print.assert_called_once_with(
                    'Invalid login attempt to your bank account. Bye !')

    def test_menu_asks_for_account_number_and_creates_account(self):
        with patch(
                'builtins.input', side_effect=('001', '001', 50.00,
                                               'q')) as mocked_input:
            with patch('builtins.print') as mocked_print:
                app_cli.menu()
                mocked_print.assert_called_once_with(
                    "Your account doesn't exists in our bank.")
                # We can even assert that our mocked method was called with the right parameters
                self.assertIn(
                    call(
                        'Welcome, lets start by accessing your bank account. Please provide your bank '
                        'account number: '), mocked_input.call_args_list)
                self.assertIn(
                    call(app_cli.MENU_PROMPT), mocked_input.call_args_list)
                self.assertIsNotNone(app_cli.current_account)

    def test_menu_calls_each_function_in_app_given_selection(self):
        with patch(
                'builtins.input',
                side_effect=('001', 'c', 'l', 'r', 'd', 'w', 'q')):
            with patch('bank_app.app_cli.ask_create_bank_account'
                       ) as mocked_create_account_func:
                with patch('bank_app.app_cli.print_accounts'
                           ) as mocked_print_accounts:
                    with patch('bank_app.app_cli.retrieve_account_balance'
                               ) as mocked_retrieve_account_balance:
                        with patch('bank_app.app_cli.ask_deposit_funds'
                                   ) as mocked_ask_deposit_funds:
                            with patch('bank_app.app_cli.ask_withdraw_funds'
                                       ) as mocked_ask_withdraw_funds:
                                app_cli.menu()

                                # We can even assert that our mocked methods were called
                                mocked_ask_deposit_funds.assert_called()
                                mocked_create_account_func.assert_called()
                                mocked_print_accounts.assert_called()
                                mocked_retrieve_account_balance.assert_called()
                                mocked_ask_withdraw_funds.assert_called()

    def test_print_accounts(self):
        with patch('builtins.print') as mocked_print:
            app_cli.current_bank.add_account(Account('001', 50.0))
            app_cli.current_bank.add_account(Account('002', 150.0))
            app_cli.print_accounts()
            # We can even assert that our mocked method was called with the right parameters
            self.assertIn(
                call("- {'account_number': '001', 'balance': 50.0}"),
                mocked_print.call_args_list)
            self.assertIn(
                call("- {'account_number': '002', 'balance': 150.0}"),
                mocked_print.call_args_list)

    def test_ask_create_bank_account(self):
        with patch(
                'builtins.input', side_effect=('001', 50.0)) as mocked_input:
            app_cli.ask_create_bank_account()
            # We can even assert that our mocked method was called with the right parameters
            self.assertIn(
                call("Enter your bank account number: "),
                mocked_input.call_args_list)
            self.assertIn(
                call("Enter your bank account balance: "),
                mocked_input.call_args_list)
            self.assertEqual(1, len(app_cli.current_bank.accounts))

    def test_ask_create_bank_account_catches_value_error_exception(self):
        with patch(
                'builtins.input',
                side_effect=('001', 'Invalid number')) as mocked_input:
            with patch('builtins.print') as mocked_print:
                app_cli.ask_create_bank_account()

                # We can even assert that our mocked method was called with the right parameters
                self.assertIn(
                    call("Enter your bank account number: "),
                    mocked_input.call_args_list)
                self.assertIn(
                    call("Enter your bank account balance: "),
                    mocked_input.call_args_list)
                mocked_print.assert_called_once_with(
                    'The amount for initial balance is not a valid number')
                self.assertEqual(0, len(app_cli.current_bank.accounts))

    @staticmethod
    def test_retrieve_balance():
        with patch('builtins.print') as mocked_print:
            app_cli.current_account = Account('001', 50.0)
            app_cli.retrieve_account_balance()
            mocked_print.assert_called_once_with(50.00)

    def test_retrieve_balance_not_calls_print(self):
        with patch('builtins.print') as mocked_print:
            app_cli.retrieve_account_balance()
            mocked_print.assert_not_called()

    def test_deposit_funds_prints_new_balance_before_done(self):
        with patch('builtins.input', return_value=30.0) as mocked_input:
            with patch('builtins.print') as mocked_print:
                app_cli.current_account = Account('001', 50.0)
                app_cli.ask_deposit_funds()
                self.assertEqual(80, app_cli.current_account.balance)
                mocked_input.assert_called_once_with(
                    "Enter the money amount to deposit: ")
                mocked_print.assert_called_once_with(
                    'The new balance for account 001 is 80.0')

    def test_deposit_funds_catches_value_error_prints_error_message(self):
        with patch(
                'builtins.input',
                return_value='not valid number') as mocked_input:
            with patch('builtins.print') as mocked_print:
                app_cli.current_account = Account('001', 50.0)
                app_cli.ask_deposit_funds()
                self.assertEqual(50, app_cli.current_account.balance)
                mocked_input.assert_called_once_with(
                    "Enter the money amount to deposit: ")
                mocked_print.assert_called_once_with(
                    'The amount to be deposited is not a valid number')

    def test_withdraw_funds_prints_new_balance_before_done(self):
        with patch('builtins.input', return_value=30.0) as mocked_input:
            with patch('builtins.print') as mocked_print:
                app_cli.current_account = Account('001', 50.0)
                app_cli.ask_withdraw_funds()
                self.assertEqual(20, app_cli.current_account.balance)
                mocked_input.assert_called_once_with(
                    "Enter the money amount to withdraw: ")
                mocked_print.assert_called_once_with(
                    'The new balance for account 001 is 20.0')

    def test_withdraw_funds_catches_value_error_prints_error_message(self):
        with patch(
                'builtins.input',
                return_value='not valid number') as mocked_input:
            with patch('builtins.print') as mocked_print:
                app_cli.current_account = Account('001', 50.0)
                app_cli.ask_withdraw_funds()
                self.assertEqual(50, app_cli.current_account.balance)
                mocked_input.assert_called_once_with(
                    "Enter the money amount to withdraw: ")
                mocked_print.assert_called_once_with(
                    'The amount to withdrawal is not a valid number')


if __name__ == "__main__":
    unittest.main()
