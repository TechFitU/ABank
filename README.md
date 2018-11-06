# ABank

ABank is a small bank web application to practice BDD and TDD. It is built with [Python][0] using the [Flask Framework][1].

This project has the following basic features:

* Retrieve bank account balance
* Deposit money into a bank account
* Withdraw money from a bank account
* Automatic log of any transaction made in a bank account 

## Installation

Clone the project source code from the repository:
    
    git clone git@github.com:TechFitU/ABank.git
    
    cd ABank

#### Set up a development environment
Quickly, first install Python 3. It comes with virtualenv built-in.

Create it by:

    $ python3 -m venv my_env

On Windows:


    > py -3 -m venv venv
    

If you needed to install virtualenv (http://flask.pocoo.org/docs/1.0/installation/#install-virtualenv) because you are on an older version of Python, use the following command instead:

On Linux, virtualenv is provided by your package manager:

   - Debian, Ubuntu

    
    sudo apt-get install python-virtualenv
    
   - CentOS, Fedora


    sudo yum install python-virtualenv
    
   - Arch


    sudo pacman -S python-virtualenv
    virtualenv venv --python=/route/to/python

   - If you are on Mac OS X or Windows, download get-pip.py, then:


    sudo python2 Downloads/get-pip.py
    sudo python2 -m pip install virtualenv

-   On Windows, as an administrator:

    \Python27\python.exe Downloads\get-pip.py
    \Python27\python.exe -m pip install virtualenv

On Windows create the virtual environment by executing:

    C:\Python27\Scripts\virtualenv.exe venv
   

#### Activate environment by running:


    $ . my_env/bin/activate

On Windows CMD prompt:

    > venv\Scripts\activate.bat

#### Install all dependencies
If you need to keep requirements.txt updated then run:

    pip install -r requirements.txt
    pip freeze > requirements.txt

## Run

    flask run
Or
 
    python -m flask run


Ready!. Open http://127.0.0.1:5000 in a browser.

    
## Develop, Contribute and Test
###Test using PyCharm
Create a sample unittest configuration in PyCharm (for example), and choose:

- `Path` as as target, with your project's `/tests` folder.

- Run the tests

###Test using Pytest and Behave and Coverage
Please code and contribute using PEP-8 specification for code style. But if its so boring, install yapf library to make it by command:

    yapf  -i -r -p -e venv .
    
Install behave, pytest and coverage libraries by running:

    pip install behave pytest pytest-cov coverage
   
Run the tests with pytest and code coverage support (reports is displayed in terminal with missing line numbers shown).
You can add add --pdb to debug every fail test.

    py.test -v -r f --cov-report term-missing --cov=bank_app/ tests/

These two report options output to files without showing anything on the terminal:

    py.test -v -r f --cov-report html --cov-report xml --cov-fail-under=95 --cov=bank_app/ tests/

Or

    coverage run -m pytest -v -r f
    coverage report --show-missing --skip-covered --fail-under=95
    
Run the acceptance tests

    behave tests/acceptance --stop --tags=pending

If you want to automate the build-testing process you should run the acceptance testing task in this way:

    behave tests/acceptance --tags=-pending

### Detailed instructions

Take a look at the docs for more information.

[0]: https://www.python.org/
[1]: https://flask.pocoo.org/
