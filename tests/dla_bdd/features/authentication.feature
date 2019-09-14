Feature: User Authentication
    As a Business Analyst,
    In order to interact with the Data Lake,
    I want follow Authentication steps
    So no one unauthenticated can access the Data Lake.

    Background:
        Given   The app is run
        
    Scenario: User login
        When    User fills in username with "mhjhamza"
        And     User fills in password with "0000"
        And     The credentials exist in the database
        Then    The user must see "Login Successful!"
        When    The credentials do not exist in the database
        Then    The user must see "No Record Found!"

    Scenario: User Sign-up
        When    User fills in email with "mhjhamza1@gmail.com"
        And     User fills in username with "mhjhamza"
        And     User fills in password with "0000"
        And     The credentials do not exist in the database
        Then    The user must see "Sign-up Successful!"

 