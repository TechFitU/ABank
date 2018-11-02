Feature: Bank web app records every transaction on every account

  @pending
  Scenario: Account added generates a new transaction record
    Given I create account "<account_number>" with balance of "<balance>"
    Then A new transaction record is created for "<account_number>"

  @pending
  Scenario: A deposit into an account records a new transaction
    Given I create account "<account_number>" with balance of "<balance>"
    And I visit the deposit page for the account "<account_number>"
    When I deposit the amount "<deposit_amount>"
    Then A new transaction record is created for "<account_number>"

  @pending
  Scenario: A withdraw from an account records a new transaction
    Given I create account "<account_number>" with balance of "<balance>"
    And I visit the deposit page for the account "<account_number>"
    When I withdraw the amount "<withdraw_amount>"
    Then A new transaction record is created for "<account_number>"