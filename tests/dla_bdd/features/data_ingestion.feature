Feature: Data Ingestion
    As a Data Scientist,
    In order to contribute to the Data Lake,
    I must be able to upload a file

    Scenario: File Upload
        Given   The user is logged-In 
        When    User enters a filename with "input/filename.txt"
        And     User fills content with "Hello World"
        Then    The file "input/filename.txt" must be stored on S3