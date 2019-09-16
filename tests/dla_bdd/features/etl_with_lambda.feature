Feature: ETL Operation on Data Lake
    As an ML Engineer,
    In order to pre-process or apply wranggling to Data Lake,
    I must be able to capatalize the file contents.

    Scenario: ETL Operation
        Given   The user is logged-In with username "mhjhamza" and password "0000"
        When    Capatalizes the content of file "filename.txt"
        And Stores the file as "filename_2.txt"
        Then The content must be in uppercase