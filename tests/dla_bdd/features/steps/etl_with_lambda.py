import sys;sys.path.append('../')
from behave import *
from src.dla import Datalake
from moto import mock_s3
import boto3

@when(u'Capatalizes the content of file "{filename}"')
def step_impl(context, filename):
    context.data_lake = Datalake()
    context.filename = filename
    with mock_s3():
        context.data_lake.upload_file(filename, "helloworld")
        context.processed_body = context.data_lake.process_file(filename)


@when(u'Stores the file as "{filename}"')
def step_impl(context, filename):
    with mock_s3():
        context.data_lake.upload_file(filename, context.processed_body)
        conn = boto3.resource('s3', region_name='us-east-1')
        _file = conn.Object(context.data_lake.BUCKET, filename).get()
        context._file = _file['Body'].read()

@then(u'The content must be in uppercase')
def step_impl(context):
    print('asdadas', context._file)
    assert context._file == b"HELLOWORLD"