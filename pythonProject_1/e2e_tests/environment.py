from behave.runner import Context
from selenium import webdriver
from page_object_models.index_page import IndexPage


def before_all(context: Context):
    context.driver = webdriver.Chrome("chromedriver.exe")
    context.index_page = IndexPage(context.driver)


def after_all(context):
    context.driver.quit()

