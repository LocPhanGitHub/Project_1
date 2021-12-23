from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


class IndexPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_username_input(self):
        element: WebElement = self.driver.find_element(By.ID, "userName")
        return element

    def select_password_input(self):
        element: WebElement = self.driver.find_element(By.ID, "userPassword")
        return element

    def select_submit_button(self):
        element: WebElement = self.driver.find_element(By.ID, "logIn")
        return element

    def select_logout_button(self):
        element: WebElement = self.driver.find_element(By.ID, "logout")
        return element

    def select_manager(self):
        select_element = self.driver.find_element(By.ID, "userRole")
        select_object = Select(select_element)
        select_object.select_by_value("manager")
        first_selected_option = select_object.first_selected_option
        return first_selected_option

    def select_employee(self):
        select_element = self.driver.find_element(By.ID, "userRole")
        select_object = Select(select_element)
        select_object.select_by_value("employee")
        first_selected_option = select_object.first_selected_option
        return first_selected_option

    def select_request_id_input(self):
        element: WebElement = self.driver.find_element(By.ID, "requestId")
        return element

    def select_user_id_input(self):
        element: WebElement = self.driver.find_element(By.ID, "userId")
        return element

    def select_expense_name_input(self):
        element: WebElement = self.driver.find_element(By.ID, "expenseName")
        return element

    def select_expense_amount_input(self):
        element: WebElement = self.driver.find_element(By.ID, "expenseAmount")
        return element

    def select_expense_detail_input(self):
        element: WebElement = self.driver.find_element(By.ID, "expenseDetail")
        return element

    def select_expense_status_input(self):
        element: WebElement = self.driver.find_element(By.ID, "expenseStatus")
        return element

    def select_manager_comment_input(self):
        element: WebElement = self.driver.find_element(By.ID, "userComment")
        return element

    def select_create_reimbursement_button(self):
        element: WebElement = self.driver.find_element(By.ID, "createReimbursementButton")
        return element
