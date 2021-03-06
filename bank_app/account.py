class Account(object):
    __slots__ = ('account_number', 'balance')

    def __init__(self, account_number, balance):
        """
        Creation method for an Account object

        :param account_number: The bank account number
        :param balance: Current account balance
        """

        if not isinstance(account_number, str):
            raise TypeError('Account number must be a str')
        self.account_number = account_number
        try:
            self.balance = float(balance)
        except (TypeError, ValueError):
            raise

    def __repr__(self):
        return "Account(id={}, balance={})".format(self.account_number,
                                                   self.balance)

    def json(self):
        """
        Retrieve the dict-like representation of an Account object, ready to serialize as JSON format

        >>> a = Account('001', 50.00)
        >>> a.json()
        {'account_number': '001', 'balance': 50.0}

        :return: dictionary representation of the Account object
        :rtype: dict
        """
        return {'account_number': self.account_number, 'balance': self.balance}

    def deposit_funds(self, money):
        """
        Add funds to a bank account object

        >>> a = Account('001', 50.0)
        >>> a.deposit_funds(30.0)
        80.0

        :param money: Amount of money to deposit
        :return: The new balance
        :rtype: float
        :raise: An exception of type ValueError if money is not a number or a string representation of a number
        """
        try:
            money = float(money)
        except (TypeError, ValueError):
            raise

        self.balance += money
        return self.balance

    def withdraw_funds(self, money):
        """
        Withdraw funds from a bank account object

        >>> a = Account('001', 50.0)
        >>> a.withdraw_funds(30.0)
        20.0

        :param money: Amount of money to withdraw
        :return: The new balance
        :rtype: float
        :raise: An exception of type ValueError if money is not a number or a string representation of a number
        """
        try:
            money = float(money)
        except (TypeError, ValueError):
            raise

        if money > 600.0:
            raise ValueError('The maximum amount allowed is 600.0 a day')
        if self.balance < money:
            raise ValueError(
                'Not enough money {} in your account to complete the withdrawal'
                    .format(self.balance))

        self.balance -= money

        return self.balance


if __name__ == "__main__":  # pragma: no cover

    # Running Your Doctests
    import doctest
    doctest.testmod()
