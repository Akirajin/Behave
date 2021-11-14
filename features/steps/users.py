from behave import *
import requests

@given('we have the application running on "{host}"')
def step_impl(context, host):
    context.response = requests.get(host)
    assert (context.response.ok, True)


@when('we request "GET" to "{host}"')
def step_impl(context, host):
    context.response = requests.get(host)




@then('we will get http status "200" with payload:')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError()


@step("we have the following user in the database")
def step_impl(context):

    for row in context.table:
        model.add_user(name=row['name'], department=row['department'])
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And we have the following user in the database
                              | name | surname |
                              | Glauber | Rocha |
                              | Jessica | Rocha |



                              GHERKIN