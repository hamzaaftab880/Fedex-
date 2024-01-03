import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@given(u'Launch Browser')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="D:\pytest_behave\pytest_behave_BDD\webdrivers/chromedriver.exe")
    context.driver.maximize_window()
    # context.driver.minimize_window()


@when(u'I Open Login Page')
def step_impl(context):

    test_url = "https://www.facebook.com/"
    context.driver.get(test_url)


@then(u'Enter the username and password')
def step_impl(context,):

    context.driver.find_element(By.ID, 'email').send_keys('hamzaaftab880@gmail.com')

    time.sleep(10)

@then(u'Enter the username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    # context.driver.find_element(By.CLASS_NAME, "input").send_keys(user)
    context.driver.find_element(By.ID, "email").send_keys('hamzaaftab880@gmail.com')
    context.driver.find_element(By.Id, "pass").send_keys('hamza12')
    context.driver.find_element(By.NAME, "login").click()

    # context.driver.find_element(By.ID, "user_pass").send_keys(pwd)
    context.driver.find_element(By.NAME, "btnK").click()
    time.sleep(10)

@then(u'Click on submit button')
def step_impl(context):
    context.driver.find_element(By.ID, "wp-submit").click()


@then(u'User will be successfully logged in')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/ul/li[1]/a").click()
    expected_url = "https://wpqa1.eniture-qa.com/wp-admin/admin.php?page=wc-settings&tab=fedex_small&section"
    url = context.driver.current_url
    if url == expected_url:
        assert True, "Login Successfull"
    else:
        assert False, "Invalid Credentials"


@then(u'User will not be successfully logged in')
def step_impl(context):
    expected_url = "https://wpqa1.eniture-qa.com/wp-admin/admin.php?page=wc-settings&tab=fedex_small&section"
    url = context.driver.current_url
    if url == expected_url:
        assert True, "Login Successfull"
    else:
        assert False, "Invalid Credentials"

