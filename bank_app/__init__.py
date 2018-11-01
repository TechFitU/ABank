import os

from flask import Flask, render_template, request, flash

from bank_app.account import Account
from bank_app.bank import Bank

BANK_INSTANCE = Bank('RANDOLPH')


def create_app(test_config=None):
    # Find the correct template folder when running from a different location
    tmpl_dir = os.path.join(
        os.path.dirname(__file__), 'templates')
    # Creating our flask app and configure it through its config dictionary
    app = Flask(__name__, template_folder=tmpl_dir, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.config.from_mapping(
        SECRET_KEY=os.urandom(16),
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    BANK_INSTANCE.add_account(Account('001', 50.00))

    @app.route('/hello', methods=('GET',))
    def hello():
        return 'Hello, World!'

    @app.route('/home', methods=('GET', 'POST'))
    def home():

        balance = None
        if request.method == 'POST':
            acc_number = request.form.get('account_number', default=None)
            data = BANK_INSTANCE.get_account(acc_number)
            if data is None:
                flash("Bank account doesn't exists", category="error")
            else:
                acc = Account(**data)
                balance = acc.balance

        return render_template('index.html', balance=balance)

    @app.route('/deposit/<string:account_number>', methods=('GET', 'POST'))
    def deposit(account_number):
        data = BANK_INSTANCE.get_account(account_number)
        balance = None
        acc = None
        if data is None:
            flash("Bank account doesn't exists", category="error")
        else:
            acc = Account(**data)
            balance = acc.balance

        if request.method == 'POST' and acc is not None:
            deposit_amount = request.form.get('deposit_number', default=None)
            try:
                acc.deposit_funds(deposit_amount)
                BANK_INSTANCE.add_account(acc)
            except (TypeError, ValueError):
                flash("Invalid data type or value for the deposit amount", category="error")
            balance = acc.balance

        return render_template('deposit.html', account_number=account_number, balance=balance)

    @app.route('/withdraw/<string:account_number>', methods=('GET', 'POST'))
    def withdraw(account_number):
        data = BANK_INSTANCE.get_account(account_number)
        balance = None
        acc = None
        if data is None:
            flash("Bank account doesn't exists", category="error")
        else:
            acc = Account(**data)
            balance = acc.balance

        if request.method == 'POST' and acc is not None:
            withdraw_amount = request.form.get('withdraw_number', default=None)
            try:
                acc.withdraw_funds(withdraw_amount)
                BANK_INSTANCE.add_account(acc)

            except (ValueError, TypeError) as ex:
                flash("Invalid data type or value for the withdrawal amount", category="error")
            balance = acc.balance
            print(balance)

        return render_template('withdraw.html', account_number=account_number, balance=balance)

    return app
