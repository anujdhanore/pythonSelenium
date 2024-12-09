Feature: Executing first bdd testcase
  Scenario Outline: Login username and password validation
    Given open HRM browser
    When enter valid credential username1 <username> and password1 <password>
    Then click login button1
    And Home page loaded successfully1
    Examples:
      | username  | password  |
      | admin | admin123 |
      | admin1  |admin1234 |