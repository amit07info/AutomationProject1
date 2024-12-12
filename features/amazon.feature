Feature: Purchase Item using Amazon
  Scenario:Login with Email and Password and add item to cart and purchase it.
    Given open the Amazon browser
    When  Try Login Successfully
    Then  test_searchproduct, test_AddtoCart and test_BuyNow
    And   test_Payment