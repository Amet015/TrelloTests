from behave import *

# use_step_matcher("re")
from steps.BoardCrud import BoardCrud


@given('Sets a POST request to "{url}"')
def step_impl(context, url):
    context.board = BoardCrud()
    context.board.set_url(url)


@step('sets the "{name}" as name')
def step_impl(context, name):
    context.board.set_name(name)


@when("Sends the Post")
def step_impl(context):
    context.board.post_response()


@then('should return a "{status_code_200}" status code as response')
def step_impl(context, status_code_200):
    assert context.board.get_response().status_code == int(status_code_200)


@step('sets a DELETE request to "{url_delete}"')
def step_impl(context, url_delete):
    url = url_delete + context.board.get_response().json()['id']
    context.board.set_url(url)


@step("sends the Delete request")
def step_impl(context):
    context.board.delete_response()
