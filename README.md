# ABank

ABank is a small bank web application to practice BDD and TDD. It is built with [Python][0] using the [Flask Framework][1].

This project has the following basic features:

* Retrieve bank account balance
* Deposit money into a bank account
* Withdraw money from a bank account
* Automatic log of any transaction made in a bank account 

## Installation

1. Clone the project source code from the repository:

    
    git clone git@github.com:TechFitU/ABank.git
    
    cd ABank 

2. Set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in.

Create it by:

    $ python3 -m venv my_env`

On Windows:


    > py -3 -m venv venv
    

If you needed to install virtualenv (http://flask.pocoo.org/docs/1.0/installation/#install-virtualenv) because you are on an older version of Python, use the following command instead:

    virtualenv venv --python=/route/to/python

On Windows:

    C:\Python27\Scripts\virtualenv.exe venv
   
3. Activate it by running:


    $ . my_env/bin/activate
 

On Windows CMD prompt:

    > venv\Scripts\activate.bat

Install all dependencies. If you need to keep requirements.txt updated then run:

    pip install -r requirements.txt

## Run

    flask run
Or
 
    python -m flask run


Ready!. Open http://127.0.0.1:5000 in a browser.

    
## Test
###Using PyCharm
Create a sample unittest configuration in PyCharm (for example), and choose:

- `Path` as as target, with your project's `/tests` folder.

- Run the tests

###Using Pytest and Behave and Coverage
Install behave, pytest and coverage libraries by running:

    pip install behave
    pip install pytest pytest-cov coverage
   
Run the unit and system tests:

    py.test -v -rf --pdb --cov bank_app/ tests/
    
Run the acceptance tests (developers run with arguments: --stop --tags=-pending):

    behave tests/acceptance

### Detailed instructions

Take a look at the docs for more information.

[0]: https://www.python.org/
[1]: https://flask.pocoo.org/
