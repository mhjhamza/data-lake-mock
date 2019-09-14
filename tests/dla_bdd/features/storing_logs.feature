Feature: Storing logs in a local file
    As a user,
    whatever actions I perform on the Data Lake,
    Every action must be logged in a local file.

    Scenario: Storing Logs
        Given   The user is logged-In
        When    Capatalizes the content of file
        Then    Logs must be stored in "logs/etl.txt" file