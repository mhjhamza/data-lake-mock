Feature: Data Ingestion
    As a Data Scientist,
    In order to contribute to the Data Lake,
    I must be able to upload a file

    Scenario: File Upload
        Given   The user is logged-In with username "mhjhamza" and password "0000"
        When    User enters a filename with "filename.txt"
        And     User fills content with "Hello World"
        Then    The file must be stored on S3