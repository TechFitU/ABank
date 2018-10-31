from bank_app.account import Account
from bank_app.bank import Bank

MENU_PROMPT = '\nEnter "c" to create a new bank account, "r" to retrieve your bank account balance, ' \
              '"d" to update/deposit the balance for an account, "w" to withdraw from your account or "q" to quit: '
POST_TEMPLATE = """
--- {} ---
{}
"""
current_bank = Bank('RANDOLPH')
current_account = None


def menu():
    account_number = input('Welcome, lets start by accessing your bank account. Please provide your bank '
                           'account number: ')

    global current_account

    if account_number != "":
        current_account = current_bank.get_account(account_number)
        if current_account is None:
            print("Your account doesn't exists in our bank.")

            current_account = ask_create_bank_account()

        selection = input(MENU_PROMPT)

        while selection != 'q':
            if selection == 'c':
                ask_create_bank_account()
            elif selection == 'l':
                print_accounts()
            elif selection == 'r':
                retrieve_account_balance()
            elif selection == 'd':
                ask_deposit_funds()
            elif selection == 'w':
                ask_withdraw_funds()
            selection = input(MENU_PROMPT)

    else:
        print("Invalid login attempt to your bank account. Bye !")


def print_accounts():
    global current_bank
    for key, account in current_bank.accounts.items():
        print('- {}'.format(account))


def ask_create_bank_account():
    account_number = input("Enter your bank account number: ")
    try:
        balance = float(input("Enter your bank account balance: "))
    except ValueError:
        print('The amount for initial balance is not a valid number')
        return None
    account = Account(account_number, balance)
    current_bank.add_account(account)
    global current_account
    current_account = account
    return account


def retrieve_account_balance():
    global current_account
    if current_account is not None:
        print(current_account.balance)


def ask_deposit_funds():
    global current_account
    try:
        funds = input("Enter the money amount to deposit: ")
        print('The new balance for account {} is {}'.format(current_account.account_number,
                                                            current_account.deposit_funds(funds)))
    except ValueError:
        print('The amount to be deposited is not a valid number')


def ask_withdraw_funds():
    global current_account
    try:
        funds = input("Enter the money amount to withdraw: ")
        print('The new balance for account {} is {}'.format(current_account.account_number,
                                                            current_account.withdraw_funds(funds)))
    except ValueError:
        print('The amount to withdrawal is not a valid number')


if __name__ == '__main__':  # pragma: no cover
    menu()
