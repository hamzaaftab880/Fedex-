Feature: Checking Warehouse page

  Background:
    Given Launch Browser
    When I Open Login Page warehouse
    Then Enter the username "admin" and password "QAtest786"
    Then Click on submit button

  Scenario: Checking the warehouse link
    Then Warehouse page will be displayed

  Scenario: Checking Add Warehouse placeholders
    Then Checking placeholders are enabled and displayed

  Scenario: Checking Add Warehouse checkboxes
    Then Checking checkboxes are enabled and working properly

  Scenario: Checking Validations on placeholders
    When I Click on submit button without entering data
    Then Validations will be displayed

  Scenario: Checking Validations with entering city name
    When I enter city name "Fayetteville"
    Then Error message with required credentials

  Scenario: Checking Validations with entering state name
    When I enter state name "GA"
    Then Error message with required credentials

  Scenario: Checking Validations with entering country name
    When I enter country name "US"
    Then Error message with required credentials

  Scenario: Adding Warehouse with new zip code
    When I click on add button and enter new zip code
    Then Warehouse successfully added

  Scenario: Adding Warehouse with existing zip code
    When I click on add button and enter existing zip code
    Then Error zip code already exists

    Scenario: Updating warehouse with new zip code
      When I click on update button and enter new zip code
      Then Warehouse updated successfully

    Scenario: Deleting warehouse
        When I click on delete button
        Then Warehouse deleted successfully

  Scenario: Checking add Dropship placeholders
    Then Checking all placeholders are enabled and displayed

  Scenario: Checking Validations on dropship placeholders
    When I Click on submit button without entering data in dropship
    Then Validations will be displayed on dropship

  Scenario: Checking Validations with entering city name in dropship
    When I enter city name "Fayetteville" in dropship
    Then Error message with required credentials dropship

  Scenario: Checking Validations with entering state name in dropship
    When I enter state name "GA" in dropship
    Then Error message with required credentials dropship

  Scenario: Checking Validations with entering country name in dropship
    When I enter country name "US" in dropship
    Then Error message with required credentials dropship

    Scenario: Checking Validations with entering zip code and checking the local delivery
      When I enter the zip code and check the local delivery checkbox
      Then Error message with required credentials dropship

  Scenario: Adding Dropship with new zip code
        When I click on add button and enter zip code dropship
        Then Dropship Successfully Added

  Scenario: Adding dropship with existing zip code
    When I click on add button and enter zip code
    Then Error zip code of dropship already exists

  Scenario: Updating dropship with new zip code
    When I click on update button and enter zip code
    Then Dropship updated successfully

  Scenario: Deleting dropship
    When I click on delete button in dropship
    Then Dropship deleted successfully
