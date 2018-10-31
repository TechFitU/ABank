import os

from flask import Flask, render_template, request

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
            acc = request.form.get('account_number', default=None)

            if acc is not None:
                balance = BANK_INSTANCE.get_account_balance(acc)

        return render_template('index.html', balance=balance)

    return app
