Feature: ETL Operation on Data Lake
    As an ML Engineer,
    In order to pre-process or apply wranggling to Data Lake,
    I must be able to capatalize the file contents.

    Scenario: ETL Operation
        Given   The user is logged-In
        When    The user selects a file "input/filename.txt"
        And     Capatalizes the content of file
        And     stores the file as "processed/filename.txt"
        Then    The file "processed/filename.txt" must be stored on S3
        And     the content must be in upper-case