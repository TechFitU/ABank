Feature: Bank web application to retrieve
  and update customer accounts

  As a customer of the bank I wish to be able to view my current balance
  and update my balance
  and withdraw from my balance

  Scenario Outline: Retrieve customer balance
    Given I create account "<account_number>" with balance of "<balance>"
    And I visit the homepage
    When I enter the account number "<account_number>"
    Then I see a balance of "<balance>"
    Examples:
      | account_number | balance |
      | 1111           | 50      |
      | 2222           | 100     |
      | 3333           | 500     |
      | 4444           | 1000    |

  Scenario: The customer can not retrieve account balance, account not exists
    Given I visit the homepage
    When I enter the account number "002"
    Then I see an error saying "Bank account doesn&#39;t exists"

  Scenario Outline: The customer must be able to deposit funds (update balance) into the bank account
    Given I create account "<account_number>" with balance of "<balance>"
    And I visit the deposit page for the account "<account_number>"
    When I deposit the amount "<deposit_amount>"
    Then I see a balance of "<new_balance>"
    Examples:
      | account_number | balance | deposit_amount | new_balance |
      | 1111           | 50.0    | 50.0           | 100.0       |

  Scenario: The customer can not deposit funds, account not exists

    Given I visit the deposit page for the account "002"
    Then I see an error saying "Bank account doesn&#39;t exists"

  Scenario: The customer can not deposit invalid amount of money into the bank account
    Given I create account "001" with balance of "50.0"
    And I visit the deposit page for the account "001"
    When I deposit the amount "pepito"
    Then I see an error saying "Invalid data type or value for the deposit amount"

  Scenario Outline: The customer must be able to withdraw funds (max: 600 per day) from the bank account.
    Given I create account "<account_number>" with balance of "<balance>"
    And I visit the withdrawal page for the account "<account_number>"
    When I withdraw the amount "<withdraw_amount>"
    Then I see a balance of "<new_balance>"
    Examples:
      | account_number | balance | withdraw_amount | new_balance |
      | 1111           | 50.0    | 50.0            | 0.0         |
      | 2222           | 100     | 100             | 0.0         |
      | 3333           | 500     | 600.0           | 500.0       |
      | 4444           | 1000    | 600.01          | 1000.0      |


  Scenario: The customer observes error messages when withdrawing funds from the bank account.
    Given I create account "001" with balance of "50.1"
    And I visit the withdrawal page for the account "001"
    When I withdraw the amount "pepito"
    Then I see an error saying "Invalid data type or value for the withdrawal amount"