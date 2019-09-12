import sys;sys.path.append('../')
from behave import *
from src.dla import Datalake

@when(u'A new user enters a  "123" and "123"')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: When A new user enters a  "123" and "123"')

@then(u'The user a "456" messege')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: Then The user a "456" messege')