import unittest
import sys
from moto import mock_s3
sys.path.append('./')
sys.path.append('../')
from src.dla import Datalake

class DataLake_TestCases(unittest.TestCase):

    def test_sign_up(self):
        username, password, email = 'hamza', '0000', 'gmail'
        self.data_lake = Datalake()
        assert self.data_lake.sign_up(
            username, password, email) == "Sign-up Successful!"

    def test_sign_in(self):
        self.test_sign_up()
        username, password = 'hamza', '0000'
        assert self.data_lake.sign_in(
            username, password) == "Login Successful!"

    @mock_s3
    def test_upload_file(self):
        self.test_sign_up()
        self.test_sign_in()
        assert self.data_lake.upload_file('input/filename.txt', 'Hello World!')

    
    def test_process_file(self):
        self.test_sign_up()
        self.test_sign_in()
        with mock_s3():
            self.test_upload_file()
            body = self.data_lake.get_file('input/filename.txt')
            assert self.data_lake.process_file('input/filename.txt') == body.upper()

    def test_verify_logs(self):
        self.test_sign_up()
        self.test_sign_in()
        assert self.data_lake.store_logs(logs_file='logs/etl.txt', content='')

if __name__ == "__main__":
    unittest.main()
