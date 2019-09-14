from behave import *
import sys
sys.path.append('./')
sys.path.append('../')
from src.dla import Datalake

@given(u'The app is run')
def step_impl(context):
    context.data_lake = Datalake()

@when(u'User fills in username with "{username}"')
def step_impl(context, username):
    context.username = username

@when(u'User fills in password with "{password}"')
def step_impl(context, password):
    context.password = password

@when(u'The credentials exist in the database')
def step_impl(context):
    with open('database.txt', 'r') as file:
        records = file.readlines()
        for record in records:
            __username, __password = record.split(',')[:2]
            if context.username == __username and context.password == __password:
                return True
        return False   

@then(u'The user must see "{output}"')
def step_impl(context, output):
    assert context.data_lake.sign_in(context.username, context.password) == output

@when(u'The credentials do not exist in the database')
def step_impl(context):
    with open('database.txt', 'r') as file:
        records = file.readlines()
        for record in records:
            __username, __password = record.split(',')[:2]
            if context.username == __username and context.password == __password:
                pass
        context.credentials_exist = False

@then(u'The user must see "{output}"')
def step_impl(context, output):
    assert context.data_lake.sign_in(context.username, context.password) == output

@when(u'User fills in email with "{email}"')
def step_impl(context, email):
    context.email = email

@then(u'The user must see "{output}"')
def step_impl(context, output):
    assert context.data_lake.sign_up(context.username, context.password, context.email) == output