Feature: Executing first bdd tetscase
  Scenario :Login username and password validation
    Given open HRM browser
    When enter valid credental username1 <username> and password1 <password>
    Then click login button1
    Then click Admin button1
    And Home page loaded successfully1
#    Examples:
#      | username  | password |
#      | Admin     | admin123 |
