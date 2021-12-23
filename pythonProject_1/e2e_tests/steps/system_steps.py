import time

from behave import Given, When, Then


@When(u'the user enters wrong username in the username input box')
def step_impl(context):
    context.index_page.select_username_input().send_keys("SomethingWrong")


@When(u'the user enters wrong password in the password input box')
def step_impl(context):
    context.index_page.select_password_input().send_keys("thisiswrong")


@Then(u'the user should not be logged in and an alert should arise to indicate that login failed')
def step_impl(context):
    time.sleep(1)
    assert context.driver.switch_to.alert.text == "Login Failed: Please Try Again!"
    context.driver.switch_to.alert.accept()


@When(u'the employee enters a negative amount into the amount input')
def step_impl(context):
    context.index_page.select_expense_amount_input().send_keys(-250)


@Then(u'A pop up alert should inform the employee their request has not been made, and there was an error about negative values')
def step_impl(context):
    time.sleep(1)
    assert context.driver.switch_to.alert.text == "Request Failed!"
    context.driver.switch_to.alert.accept()


@When(u'the employee enters an non-numeric amount into the amount input')
def step_impl(context):
    context.index_page.select_expense_amount_input().send_keys("two hundred")


@Then(u'A pop up alert should inform the employee their request has not been made, and there was an error about non-numeric values amount entered')
def step_impl(context):
    time.sleep(1)
    assert context.driver.switch_to.alert.text == "Request Failed!"
    context.driver.switch_to.alert.accept()
