import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

@pytest.fixture()
def driver():
    # Set up WebDriver
    global driver1
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service = Service("C:\\Users\\anuj.dhanore_infobea\\Downloads\\chromedriver-win64\\chromedriver.exe")
    driver1 = webdriver.Chrome(options=options, service=service)
    driver1.implicitly_wait(5)
    driver1.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver1.maximize_window()

# Parameterize test with different usernames and passwords
@pytest.mark.parametrize(
    "username, password",
    [
        ("Admin", "admin123"),       # Valid credentials
        ("invalid_user", "admin123"), # Invalid username
        ("Admin", "wrongpassword"),  # Invalid password
        ("", ""),                    # Empty credentials
    ]
)

def test_login(driver, username, password):
    # Locate and interact with username field
    username_field = driver1.find_element("name", "username")
    username_field.send_keys(username)

    # Locate and interact with password field
    password_field = driver1.find_element("name", "password")
    #password_field.clear()
    password_field.send_keys(password)

    # Click login button
    login_button = driver1.find_element("xpath", "//button[@type='submit']")
    login_button.click()

    driver1.close()