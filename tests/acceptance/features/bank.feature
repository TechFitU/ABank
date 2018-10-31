Feature: Bank web application to retrieve
  and update customer accounts

  As a customer of the bank I wish to be able to view my current balance
  and update my balance
  and withdraw from my balance

  Scenario: Customer retrieves balance successfully
    Given I visit the homepage
    And account number "0001" is a valid account with balance of "50"
    When I enter the account number "0001"
    Then the balance of the account is "50"