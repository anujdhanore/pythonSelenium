Feature: Open Demo web shop and add product to cart then checkout
  Scenario: Open Demo web shop and add product to cart
    Given Open web shop
    When  Add notebook to the cart
    Then  Ensure product added to cart
    