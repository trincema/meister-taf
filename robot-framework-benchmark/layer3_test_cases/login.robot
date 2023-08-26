# Given a user is on the login page
# When the user enters their username and password and clicks the login button
# Then the user should be directed to the home page.

*** Settings ***
Resource               ../layer2_keywords/login_keywords.resource

*** Variables ***
${VALID_USERNAME}      emanuel.trinc@yahoo.com
${VALID_PASSWORD}      Meister12345678

*** Test Cases ***
Valid Login MindMeister
    Given I am on the MindMeister login page
    When I login to MindMeister with username "${VALID_USERNAME}" and password "${VALID_PASSWORD}"
    Then I should see the MindMeister profile page

