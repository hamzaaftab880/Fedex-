Feature: Check Connection Settings Page

  Background:
    Given Launch Browser
    When I Open Login Page
    Then Enter the username "admin" and password "QAtest786"
    Then Click on submit button


  Scenario: Check Connection Settings Page Link
    When I Click on connection settings link
    Then Connection settings page will appear
#
  Scenario: Testing Connection with Valid Credentials
    When I enter plugin license key "RSM7S0ZZ-54A4AJJ9-ZI8MEIRH-BPX1NO4N"
    And I enter billing address
    And I enter account no "748465669"
    And I enter meter no "251345779"
    And I enter production password "cMRMt1ui4jPmvPUmc2hqIaTUD"
    And I enter authentication key "l8BMUH0ME2W2mGYM"
    And I enter shipper account number "748465669"
    And I enter third party account number "669103611"
    Then Success message will appear

  Scenario Outline: Testing Connection with Invalid Credentials
    When I enter plugin license key "<plugin_key>"
    And I enter billing address
    And I enter account no "<account_no>"
    And I enter meter no "<meter_no>"
    And I enter production password "<password>"
    And I enter authentication key "<auth_key>"
    And I enter shipper account number "<shipper_no>"
    And I enter third party account number "<third_party>"
    Then Error message will appear

    Examples:
      | account_no   | |          password         |  | meter_no  | |      auth_key      | |             plugin_key             | |  shipper_no  | |  third_party |
      | 74846569     | |cMRMt1ui4jPmvPUmc2hqIaTUD  |  | 251345779 | | l8BMUH0ME2W2mGYM   | | RSM7S0ZZ-54A4AJJ9-ZI8MEIRH-BPX1NO4N| |748465669    | |   669103611  |
      | 748465669    | |cMRMt1ui4jPmvPUmc2hqaTUD   |  | 251345779 | | l8BMUH0ME2W2mGYM   | | RSM7S0ZZ-54A4AJJ9-ZI8MEIRH-BPX1NO4N| |748465669    | |   669103611  |
      | 748465669    | |cMRMt1ui4jPmvPUmc2hqIaTUD  |  | 25134779  | | l8BMUH0ME2W2mGYM   | | RSM7S0ZZ-54A4AJJ9-ZI8MEIRH-BPX1NO4N| |748465669    | |   669103611  |
      | 748465669    | |cMRMt1ui4jPmvPUmc2hqIaTUD  |  | 251345779 | | l8BUH0ME2W2mGYM    | | RSM7S0ZZ-54A4AJJ9-ZI8MEIRH-BPX1NO4N| |748465669    | |   669103611  |
      | 748465669    | |cMRMt1ui4jPmvPUmc2hqIaTUD  |  | 251345779 | | l8BMUH0ME2W2mGYM   | | RSMS0ZZ-54A4AJJ9-ZI8MEIRH-BPX1NO4N | |748465669    | |   669103611  |
      | 748465669    | |cMRMt1ui4jPmvPUmc2hqIaTUD  |  | 251345779 | | l8BMUH0ME2W2mGYM   | | RSM7S0ZZ-54A4AJJ9-ZI8MEIRH-BPX1NO4N| |74865669     | |   669103611  |
      | 748465669    | |cMRMt1ui4jPmvPUmc2hqIaTUD  |  | 251345779 | | l8BMUH0ME2W2mGYM   | | RSM7S0ZZ-54A4AJJ9-ZI8MEIRH-BPX1NO4N| |748465669    | |   66913611   |


    Scenario: Checking validations on placeholders
      When I leave all spaces blank
      Then Error will be shown with required data