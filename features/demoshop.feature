Feature: Add item to cart
  Scenario:Login with Email and Password and add item to cart
    Given open demowebshop web
    When  Navigate to Registration page and Fill all the mendatory details and click register
    Then  Navigate to Log in page and Enter valid credential Email "amitsharma7@gmail.com" and password "admin123"
    Then  click on Computer and click to Notebooks
    Then  click on Add to Cart
    Then  Go to Shopping Cart and click on Check out
    Then  Enter Details and Click on Continue
    Then  Click on Confirm
    And   Click on Continue