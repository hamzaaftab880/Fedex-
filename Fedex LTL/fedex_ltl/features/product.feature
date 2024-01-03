Feature: Checking Warehouse page

  Background:
    Given Launch Browser
    When Opening product page
    Then Enter the username "admin" and password "QAtest786"
    Then Click on submit button
    When I open product page

  Scenario: Checking checkboxes are displayed and enabled on products page
   And I verify the placeholders are displayed and enabled
    When I verify that fedex ltl is showing in dropdown menu


