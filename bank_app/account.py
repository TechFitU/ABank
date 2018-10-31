class Account(object):
    __slots__ = ('account_number', 'balance')

    def __init__(self, account_number, balance):
        """
        Creation method for an Account object

        :param account_number: The bank account number
        :param balance: Current account balance
        """

        self.account_number = account_number
        self.balance = balance

    def __repr__(self):
        return "Account(id={}, balance={})".format(self.account_number, self.balance)

    def json(self):
        """
        Retrieve the dict-like representation of an Account object, ready to serialize as JSON format

        >>> a = Account('001', 50.00)
        >>> a.json()
        {'account_number': '001', 'balance': 50.00}

        :return: dictionary representation of the Account object
        :rtype: dict
        """
        return {
            'account_number': self.account_number,
            'balance': self.balance
        }

    def deposit_funds(self, money):
        """
        Add funds to a bank account object

        >>> a = Account('001', 50.0)
        >>> a.deposit_funds(30.0)
        80

        :param money: Amount of money to deposit
        :return: The new balance
        :rtype: float
        :raise: An exception of type ValueError if money is not a number or a string representation of a number
        """
        self.balance += float(money)
        return self.balance

    def withdraw_funds(self, money):
        """
        Withdraw funds from a bank account object

        >>> a = Account('001', 50.0)
        >>> a.withdraw_funds(30.0)
        20

        :param money: Amount of money to withdraw
        :return: The new balance
        :rtype: float
        :raise: An exception of type ValueError if money is not a number or a string representation of a number
        """

        self.balance -= float(money)

        return self.balance


if __name__ == "__main__":  # pragma: no cover

    # Running Your Doctests
    import doctest

    doctest.testmod()
