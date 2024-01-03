Feature: Login Page

  Background: Common steps of login page
    Given Launch Browser
    When I Open Login Page


  Scenario: Check Login details with Valid Credentials
    Then Enter the username and password
    Then Click on submit button
    Then User will be successfully logged in
#
#  Scenario Outline: Check Login details with Invalid Credentials
#    Then Enter the username "<username>" and password "<password>"
#    Then Click on submit button
#    Then User will not be successfully logged in
#
#
#    Examples:
#      | username | | password |
#      | admin123 | | QAtest7861 |
#      | QAtest786 | | admin |
#      | admin | | admin |
#      | admin | | QAtest786 |



