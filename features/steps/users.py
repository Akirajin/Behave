from behave import *
import requests

@given('we have the application running on "{host}"')
def step_impl(context, host):
    context.response = requests.get(host)


@given('we have postgreSQL running on "{host}"')
def step_impl(context, host):
    pass

@when('we have the following user in the database')
def step_impl(context, verb, request):
    assert True is not False


@when('we request "GET" to "{host}"')
def step_impl(context, verb, request):
    assert True is not False


@step("we have the following user in the database")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError()


@then('we will get http status "200" with payload:')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError()