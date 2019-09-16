import sys;sys.path.append('../')
from behave import *
from src.dla import Datalake
from moto import mock_s3

@given(u'The user is logged-In with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.data_lake = Datalake()
    context.data_lake.sign_in(username, password)

@when(u'User enters a filename with "{filename}"')
def step_impl(context, filename):
    context.filename = filename

@when(u'User fills content with "{content}"')
def step_impl(context, content):
    context.content = content

@then(u'The file must be stored on S3')
def step_impl(context):
    with mock_s3():
        assert context.data_lake.upload_file(context.filename, context.content)