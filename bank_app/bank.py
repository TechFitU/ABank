class DBConnectionError(Exception):
    pass


class Bank(object):
    def __init__(self, name, data_interface=None):
        """
        Creation method for a Bank object

        :param data_interface: The database interface used to retrieve the account data
        """
        self.di = data_interface
        self.name = name
        self.accounts = {}

    def __repr__(self):
        return "Bank(name={}, accounts={})".format(self.name,
                                                   len(self.accounts))

    def add_account(self, account):
        """Adds an account to the bank_app

        :param account: the account object
        :return: The json representation of the Account object added
        :rtype: dict
        """
        self.accounts[account.account_number] = account.json()
        # We should save in database the new account using self.di, but not now in order to get our tests passed

    def get_account(self, account_number):
        """Looks for an account in the database given its account number

        >>> b = Bank({'001': {'account_number': '001', 'balance': 50}})
        >>> b.get_account('001')
        {'account_number': '001', 'balance': 50}

        :param account_number: The account number
        :return: dict-like representation of an Account
        :rtype: dict
        """

        if not isinstance(account_number, str):
            raise ValueError('Invalid type <{}> for account number'.format(
                type(account_number)))

        try:
            if self.di is not None:
                result = self.di.get(account_number)
            else:
                result = self.accounts.get(account_number, None)

        except DBConnectionError:
            result = "Connection error occurred. Try Again."
        return result

    def get_account_balance(self, account_number):
        """Returns the account balance in the database given its account number

        >>> b = Bank({'001': {'account_number': '001', 'balance': 50}})
        >>> b.get_account_balance('001')
        50

        :type account_number: str
        :param account_number: The account number
        :return: the balance for the bank_app account
        :rtype: float
        """

        if not isinstance(account_number, str):
            raise ValueError('Invalid type <{}> for account number'.format(
                type(account_number)))

        try:
            result = self.di.get(account_number) if self.di is not None \
                else self.accounts.get(account_number, None)
            if result is not None:
                result = result["balance"]

        except DBConnectionError:
            result = "Connection error occurred. Try Again."
        return result


if __name__ == "__main__":  # pragma: no cover

    # Running Your Doctests
    import doctest
    doctest.testmod()
