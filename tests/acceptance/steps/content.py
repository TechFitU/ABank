# -*- coding: utf-8 -*-
from behave import *
from nose.tools import assert_equal, assert_in
from webtest import TestApp

from bank_app import create_app, BANK_INSTANCE
from bank_app.account import Account

use_step_matcher('re')


@given(u'I visit the homepage')
def i_visit_the_homepage(context):
    app = create_app({'TESTING': True})
    context.browser = TestApp(app)

    context.response = context.browser.get('/home')
    assert_equal(200, context.response.status_code)


@given(u'account number "([^"]*)" is a valid account with balance of "([^"]*)"')
def step_impl(context, account_number, balance):
    account = Account(account_number, balance)
    BANK_INSTANCE.add_account(account)


@when(u'I enter the account number "([^"]*)"')
def step_impl(context, account_number):
    form = context.response.forms['account-form']
    form['account_number'] = account_number
    context.form_response = form.submit()
    assert_equal(context.form_response.status_code, 200)


@then(u'the balance of the account is "([^"]*)"')
def then_i_see_a_balance_of_group1(context, expected_balance):
    assert_in("Balance: {}".format(expected_balance), context.form_response.text)
