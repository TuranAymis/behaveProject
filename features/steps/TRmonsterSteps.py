from lib2to3.fixes.fix_input import context

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@given('I launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

@when('I open monster tr login page')
def step_impl(context):
    context.driver.get("https://www.monsternotebook.com.tr/giris/")

@when('Accept Onetrust')
def step_impl(context):
    context.driver.find_element(By.ID,"onetrust-accept-btn-handler").click()
    context.driver.implicitly_wait(5)

@when('Enter mail "{user}" and password "{pwd}"')
def step_impl(context,user,pwd):
    element = context.driver.find_element(By.ID,"Password")
    context.driver.execute_script("arguments[0].scrollIntoView()", element)
    context.driver.find_element(By.ID,"UserNameOrEmail").send_keys(user)
    context.driver.find_element(By.ID,"Password").send_keys(pwd)
    context.driver.implicitly_wait(5)

@when('Click login button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//button[text()='GİRİŞ YAP']").click()
    context.driver.implicitly_wait(5)

@then('User must successfully login to website')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//div[text()='test turan']").is_displayed()

@then('Close browser')
def step_impl(context):
    context.driver.close()
