*** Settings ***
Library    ../resources/PythonPageObjects.py

Suite Setup       Open Browser
Suite Teardown    Close Browser
Test Teardown     Run Keyword And Ignore Error    Capture Failure Screenshot    ${TEST STATUS}

*** Test Cases ***
Checkout Successfully
    Given User Open SauceDemo Login Page
    When User Login With    standard_user    secret_sauce
    And User Adds Product    Sauce Labs Backpack
    And User Go To Cart
    And User Checkout With    John    Doe    12345
    Then Checkout Should Be Successful
