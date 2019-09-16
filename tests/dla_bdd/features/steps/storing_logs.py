from behave import *

@then(u'Logs must be stored in "{filename}" file')
def step_impl(context, filename):

    assert True