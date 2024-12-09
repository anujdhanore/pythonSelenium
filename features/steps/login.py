import logging

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

@given(u'open HRM browser')
def step_impl(context):

    global  driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    #options.add_argument('--headless')
    s = Service("C:\\Users\\anuj.dhanore_infobea\\Downloads\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=s)
    driver.implicitly_wait(5)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()

@when(u'enter valid credential username1 {un} and password1 {pw}')
def step_impl(context, un, pw):
    driver.find_element("name", "username").send_keys(un)
    driver.find_element("name", "password").send_keys(pw)

@then(u"click login button1")
def step_impl(context):
    driver.find_element("xpath", "//button[@type='submit']").click()
    print("Login success")

@then(u'Home page loaded successfully1')
def step_impl(context):
    logger.info("Login success")
    #driver.quit()
