"""Data Lake class."""

from datetime import datetime
from moto import mock_s3
import boto3
import logging


class Datalake:
    """Datalake class for all the data lake related operations."""

    def __init__(self):
        """Initialize the data_lake object."""
        
        self.DB_CONN = 'database.txt'
        self.APPEND_MODE = 'a'
        self.READ_MODE = 'r+'
        self.current_user = ''
        
        # Responses
        self.NO_RECORD_FOUND = "No Record Found!"
        self.LOGIN_SUCCESSFUL = "Login Successful!"
        self.SIGN_UP_SUCCESSFUL = "Sign-up Successful!"

        # ETL Logs
        self.SIGN_UP_LOG = '{} signed-up'
        self.LOGGED_IN_LOG = '{} logged-in'
        self.FILE_CREATED = '{} created a file {}'
        self.FILE_PROCESSED = '{} processed a file {}'
        self.BUCKET = 'datalake_raw'

    def store_logs(self, logs_file='logs/etl.txt', content=''):
        with open(logs_file, self.APPEND_MODE) as logs:
            log = content + ' at {0} \n'.format(datetime.now())
            logs.write(log)
            logging.info(log, logging.INFO)
        return True

    def sign_up(self, username='', password='', email=''):
        if not (username and password and email):
            raise ValueError()
        with open(self.DB_CONN, self.APPEND_MODE) as file:
            file.write('{},{},{}\n'.format(username, password, email))
        self.store_logs(content=self.SIGN_UP_LOG.format(
            username))
        return self.SIGN_UP_SUCCESSFUL

    def sign_in(self, username='', password=''):
        with open(self.DB_CONN, self.READ_MODE) as file:
            records = file.readlines()
            for record in records:
                __username, __password = record.split(',')[:2]
                if username == __username and password == __password:
                    self.store_logs(content=self.LOGGED_IN_LOG.format(
                        username))
                    self.current_user = username
                    return self.LOGIN_SUCCESSFUL
            return self.NO_RECORD_FOUND

    def upload_file(self, filename, body):
        conn = boto3.resource('s3', region_name='us-east-1')
        conn.create_bucket(Bucket=self.BUCKET)
        response = boto3.client('s3', region_name='us-east-1')\
            .put_object(Bucket=self.BUCKET, Key=filename, Body=body)
        self.store_logs(content=self.FILE_CREATED.format(
            self.current_user, filename))
        return response['ResponseMetadata']['HTTPStatusCode'] == 200

    def process_file(self, filename):
        conn = boto3.resource('s3', region_name='us-east-1')
        _file = conn.Object(self.BUCKET, filename).get()
        self.store_logs(content=self.FILE_PROCESSED.format(
            self.current_user, filename))
        return _file['Body'].read().upper()

    def get_file(self, filename):
        conn = boto3.resource('s3', region_name='us-east-1')
        _file = conn.Object(self.BUCKET, filename).get()
        return _file['Body'].read()


if __name__ == "__main__":

    data_lake = Datalake()

    with mock_s3():
        a = data_lake.upload_file('filename', 'boasdadadasdy')
        print('status', a)
        conn = boto3.resource('s3', region_name='us-east-1')
        obj = conn.Object(data_lake.BUCKET, 'filename').get()
        print('bodyyy', obj['Body'].read())
        processed_body = data_lake.process_file('filename')
        data_lake.upload_file('filename', processed_body)
        obj = conn.Object(data_lake.BUCKET, 'filename').get()
        print('newbodyyy', obj['Body'].read())