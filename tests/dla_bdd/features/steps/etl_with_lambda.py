from behave import * 

@when(u'The user selects a file "input/filename.txt"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The user selects a file "input/filename.txt"')


@when(u'Capatalizes the content of file')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Capatalizes the content of file')


@when(u'stores the file as "processed/filename.txt"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When stores the file as "processed/filename.txt"')


@then(u'The file "processed/filename.txt" must be stored on S3')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The file "processed/filename.txt" must be stored on S3')


@then(u'the content must be in upper-case')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the content must be in upper-case')