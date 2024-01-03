Feature: Quote Settings Page

  Background:
    Given Launch Browser
    When I Open Login Page
    Then Enter the username "admin" and password "QAtest786"
    Then Click on submit button
    When I Click on quote settings page link

  Scenario:Checking RAD link is working fine
    Then I verify rad link

  Scenario:Checking RAD learn more link is working fine
    Then I verify rad learn more link

  Scenario:Checking lift gate link is working fine
    Then I verify lift gate link

  Scenario:Checking lift gate learn more link is working fine
    Then I verify lift gate learn more link

  Scenario:Checking freight direct link is working fine
    Then I verify freight direct link

  Scenario:Checking freight direct services is working fine
    Then I verify freight direct services link

  Scenario:Checking shipping slug link is working fine
    Then I verify shipping slug link

  Scenario: Checking all the placeholders are displayed and enabled
    Then I Verify all placeholders

  Scenario: Checking all select all checkboxes are working fine
    Then I click on select all checkbox all checkboxes would be checked

  Scenario: Checking all checkbox is working fine
    When I verify all checkboxes are displayed enabled and selected

    Scenario: Checking all the radio buttons are working fine
      And I verify all the radio buttons are enabled
      And I verify all radio buttons are working properly