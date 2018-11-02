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


@given(u'I create account "([^"]*)" with balance of "([^"]*)"')
def i_create_account_with_balance_of_group1(context, account_number, balance):
    account = Account(account_number, float(balance))
    BANK_INSTANCE.add_account(account)


@when(u'I enter the account number "([^"]*)"')
def when_i_enter_the_account_number_group1(context, account_number):
    form = context.response.forms['account-form']
    form['account_number'] = account_number
    context.form_response = form.submit()
    assert_equal(context.form_response.status_code, 200)


@then(u'I see a balance of "([^"]*)"')
def then_i_see_a_balance_of_group1(context, expected_balance):
    assert_in("Balance: {}".format(expected_balance),
              context.form_response.text)


@then(u'I see an error saying "([^"]*)"')
def then_i_see_an_error_group1(context, message):
    if hasattr(context, 'form_response'):
        page_content = context.form_response.text
    elif hasattr(context, 'response'):
        page_content = context.response.text

    assert_in(message, page_content)


@given(u'I visit the deposit page for the account "([^"]*)"')
def step_impl(context, account_number):
    app = create_app({'TESTING': True})
    context.browser = TestApp(app)

    context.response = context.browser.get(
        '/deposit/{}'.format(account_number))
    assert_equal(200, context.response.status_code)


@when(u'I deposit the amount "([^"]*)"')
def step_impl(context, deposit_amount):
    form = context.response.forms['deposit-form']
    form['deposit_number'] = deposit_amount
    context.form_response = form.submit()
    assert_equal(context.form_response.status_code, 200)


@given(u'I visit the withdrawal page for the account "([^"]*)"')
def step_impl(context, account_number):
    app = create_app({'TESTING': True})
    context.browser = TestApp(app)

    context.response = context.browser.get(
        '/withdraw/{}'.format(account_number))
    assert_equal(200, context.response.status_code)


@when(u'I withdraw the amount "([^"]*)"')
def step_impl(context, withdraw_amount):
    form = context.response.forms['deposit-form']
    form['withdraw_number'] = withdraw_amount
    context.form_response = form.submit()
    assert_equal(context.form_response.status_code, 200)
