import sys;sys.path.append('../')
from behave import *
from src.dla import Datalake

@given(u'The user is logged-in')
def step_impl(context):
    assert context.data_lake.sign_in(context.username, context.password) == output


@when(u'User enters a filename with "input/filename.txt"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enters a filename with "input/filename.txt"')


@when(u'User fills content with "Hello World"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User fills content with "Hello World"')


@then(u'The file "input/filename.txt" must be stored on S3')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The file "input/filename.txt" must be stored on S3')