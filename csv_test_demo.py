import time
import pytest
import csv
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


# Fixture to set up WebDriver
@pytest.fixture(scope="function")
def startup():
    global driver
    # Set up WebDriver
    options = webdriver.ChromeOptions()
    # service = Service("C:\\Users\\anuj.dhanore_infobea\\Downloads\\chromedriver-win64\\chromedriver.exe")  # Update the path to your chromedriver
    driver = webdriver.Chrome(service=Service(), options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)

def config_data():
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)  # Returns the content as a dictionary"""

# Function to fetch test data from the specified CSV file
def get_csv_data(file_path):
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        return [row for row in reader]  # Returns a list of dictionaries


# Test using data from CSV
def test_example(startup):
    # Specify the path to your CSV file
    csv_file_path = r"C:\Users\anuj.dhanore_infobea\PycharmProjects\test_files\Book1.csv"

    # Fetch test data from the CSV file
    test_data_list = get_csv_data(csv_file_path)

    for test_data in test_data_list:
        uname = test_data["username"]
        pwd = test_data["password"]

        # Open the URL
        driver.get(config_data()["url"])

        # Test steps
        driver.find_element("name", "username").send_keys(uname)
        driver.find_element("name", "password").send_keys(pwd)

        driver.find_element("xpath", "//button[@type='submit']").click()

        time.sleep(2)
        # Navigate back to reset for the next test case
        driver.back()