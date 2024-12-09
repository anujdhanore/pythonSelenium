import time
import pytest
import yaml
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


# Fixture to set up WebDriver
@pytest.fixture()  # Ensures that the driver is created for each test function
def startup():
    global driver
    # Set up WebDriver
    options = webdriver.ChromeOptions()
    # service = Service("C:\\Users\\anuj.dhanore_infobea\\Downloads\\chromedriver-win64\\chromedriver.exe")  # Update the path to your chromedriver
    driver = webdriver.Chrome(service=Service(), options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver
    driver.quit()
    # Cleanup code: Quit the driver after the test


# Fixture to load data from the YAML file
"""@pytest.fixture(scope="session")
def config_data_y():
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)  # Returns the content as a dictionary"""


#@pytest.fixture(scope="session")
def config_data_j():
    with open("config.json", "r") as file:
        return json.load(file)["test_cases"]  # Returns the content as a dictionary


# Parameterize tests with data from the JSON file
@pytest.mark.parametrize("test_case", config_data_j())
def test_example_j(startup, test_case):
    # Use data from the YAML configuration
    url = test_case["url"]
    username = test_case["username"]
    password = test_case["password"]

    # Open the URL
    driver.get(url)

    # Test steps
    driver.find_element("name", "username").send_keys(username)
    driver.find_element("name", "password").send_keys(password)
    driver.find_element("xpath", "//button[@type='submit']").click()
