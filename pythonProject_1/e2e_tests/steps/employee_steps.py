from behave import Given, When, Then
import time

# e2e_tests/feature_files/employee.feature
# e2e_tests/feature_files/manager.feature
# e2e_tests/feature_files/system.feature


@Given(u'the user is on the login page')
def step_impl(context):
    context.driver.get("file:///D:/Downloads/New folder/HTML/login.html")


@When(u'the user enters their username in the username input box')
def step_impl(context):
    context.index_page.select_username_input().send_keys("Spiderman")


@When(u'the user enters their password in the password input box')
def step_impl(context):
    context.index_page.select_password_input().send_keys("spooderman")


@When(u'the user chose employee from dropbox')
def step_impl(context):
    context.index_page.select_employee().click()
    time.sleep(1)


@When(u'the user clicks the submit button')
def step_impl(context):
    context.index_page.select_submit_button().click()
    time.sleep(1)


@When(u'the user were redirected to employee home page')
def step_impl(context):
    context.driver.get("file:///D:/Downloads/New folder/HTML/employee_homepage.html")


@Then(u'the user should be logged in')
def step_impl(context):
    time.sleep(1)
    title = context.driver.title
    assert title == "Employee Homepage"


@Given(u'the employee is on the employee homepage')
def step_impl(context):
    context.driver.get("file:///D:/Downloads/New folder/HTML/employee_homepage.html")


@When(u'the employee enters his user id into the id input section')
def step_impl(context):
    context.index_page.select_user_id_input().send_keys(3)


@When(u'the employee enters a name into the expense name input')
def step_impl(context):
    context.index_page.select_expense_name_input().send_keys("E2E test")


@When(u'the employee enters an amount into the amount input')
def step_impl(context):
    context.index_page.select_expense_amount_input().send_keys(250)


@When(u'the employee enters a reason into the reason input')
def step_impl(context):
    context.index_page.select_expense_detail_input().send_keys("used for E2E test")


@When(u'the employee enters the status of the request')
def step_impl(context):
    context.index_page.select_expense_status_input().send_keys("pending")


@When(u'the employee enters blank for the manager comment')
def step_impl(context):
    context.index_page.select_manager_comment_input().send_keys("NA")


@When(u'the employee clicks the submit reimbursement button to create reimbursement')
def step_impl(context):
    context.index_page.select_create_reimbursement_button().click()
    time.sleep(1)


@Then(u'A pop up alert should inform the employee their request has been made')
def step_impl(context):
    assert context.driver.switch_to.alert.text == "Request Submitted Successful!"
    context.driver.switch_to.alert.accept()


@Given(u'the user is on their homepage')
def step_impl(context):
    context.driver.get("file:///D:/Downloads/New folder/HTML/employee_homepage.html")


@When(u'the user clicks the logout button')
def step_impl(context):
    context.index_page.select_logout_button().click()
    time.sleep(.5)


@When(u'the user were redirected back to their login page')
def step_impl(context):
    context.driver.get("file:///D:/Downloads/New folder/HTML/login.html")


@Then(u'the user should be logged out')
def step_impl(context):
    time.sleep(.5)
    assert context.driver.title == "Home Page"

