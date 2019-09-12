import sys;sys.path.append('../')
from behave import *
from src.dla import Datalake

@given('The app is run')
def step_impl(context):
    context.datalake = Datalake()

@when('A new user enters a valid "{username}" and "{password}"')
def step_impl(context, username, password):
    context.signup_result = context.datalake.signup(username, password)

@when(u'The "{username}" and "{password}" is saved in "{file_name}" file')
def step_impl(context, username, password, file_name):
    print("When The 'username' and 'password' is saved in 'database.txt' file")

@then(u'The user recieves a "{welcome}" messege')
def step_impl(context, welcome):
    assert context.signup_result.__contains__(welcome)