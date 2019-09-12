Feature: Signup-Signin
    Enabling user to Signup and then Signin

    Scenario: User Sign Up Sign In
    Given The app is run
    When A new user enters a valid "Hamza" and "123"
    And The "Hamza" and "123" is saved in "database.txt" file
    Then The user recieves a "Welcome" messege