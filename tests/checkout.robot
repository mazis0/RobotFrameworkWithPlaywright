*** Settings ***
Library    ../resources/PythonPageObjects.py

Suite Setup       Open Browser
Suite Teardown    Close Browser
Test Teardown     Run Keyword And Ignore Error    Capture Failure Screenshot    ${TEST STATUS}

*** Test Cases ***
Checkout Successfully
    Given User Open SauceDemo Login Page
    When I login with username "standard_user" and password "secret_sauce"
    And User adds product "Sauce Labs Backpack"
    And User Go To Cart
    And User completes checkout using first name "John", last name "Doe", and zip code "12345"
    Then Checkout Should Be Successful


*** Keywords ***
I login with username "${username}" and password "${password}"
     When User Login With    ${username}    ${password}
     
User adds product "${product}"
     And User Adds Product    ${product}

User completes checkout using first name "${firstname}", last name "${lastname}", and zip code "${zipcode}"
     And User Checkout With    ${firstname}    ${lastname}    ${zipcode}  
