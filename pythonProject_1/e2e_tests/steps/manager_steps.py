from behave import Given, When, Then
import time


@When(u'the manager enters their username in the username input box')
def step_impl(context):
    context.index_page.select_username_input().send_keys("TonyStark")


@When(u'the manager enters their password in the password input box')
def step_impl(context):
    context.index_page.select_password_input().send_keys("qwerty")


@When(u'the manager chose manager from dropbox')
def step_impl(context):
    context.index_page.select_manager().click()
    time.sleep(1)


@When(u'the manager were redirected to manager home page')
def step_impl(context):
    context.driver.get("file:///D:/Downloads/New folder/HTML/manager_homepage.html")


@When(u'the manager clicks the submit button')
def step_impl(context):
    context.index_page.select_submit_button().click()
    time.sleep(1)


@Then(u'the manager should be logged in')
def step_impl(context):
    time.sleep(1)
    title = context.driver.title
    assert title == "Manager Homepage"


@Given(u'the manager is on the manager homepage')
def step_impl(context):
    context.driver.get("file:///D:/Downloads/New folder/HTML/manager_homepage.html")


@When(u'the manager enters the request id into the request id input section')
def step_impl(context):
    context.index_page.select_request_id_input().send_keys(7)


@When(u'the manager enters the user id into the id input section')
def step_impl(context):
    context.index_page.select_user_id_input().send_keys(3)


@When(u'the manager enters the name into the expense name input')
def step_impl(context):
    context.index_page.select_expense_name_input().send_keys("test")


@When(u'the manager enters the amount into the amount input')
def step_impl(context):
    context.index_page.select_expense_amount_input().send_keys(200)


@When(u'the manager enters the reason into the reason input')
def step_impl(context):
    context.index_page.select_expense_detail_input().send_keys("test")


@When(u'the manager edits the status of the request')
def step_impl(context):
    context.index_page.select_expense_status_input().send_keys("accepted")


@When(u'the manager enters the manager comment')
def step_impl(context):
    context.index_page.select_manager_comment_input().send_keys("Accepted")


@When(u'the manager clicks the submit reimbursement button to update the reimbursement')
def step_impl(context):
    context.index_page.select_create_reimbursement_button().click()
    time.sleep(1)


@Then(u'A pop up alert should inform the manager the request has been updated')
def step_impl(context):
    assert context.driver.switch_to.alert.text == "Request Updated Successful!"
    context.driver.switch_to.alert.accept()




