from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
import allure


# FrameWork-PyTestFrameWork
@pytest.fixture()
def test_verifyURL():
    global driver

    options = webdriver.ChromeOptions()
    options.add_experimental_option(name="detach",
                                    value=True)  # using this statement to stable the browser (not close automatically)
    s = Service("C:\\Users\\anuj.dhanore_infobea\\Downloads\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=s)
    driver.implicitly_wait(5)
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()

@allure.feature("Testing allure")
@pytest.mark.regression
@pytest.mark.books
def test_clickBooks(test_verifyURL):
    expected_title = "Demo Web Shop"
    actual_title = driver.title
    # Assert that the actual title matches the expected title
    assert actual_title == expected_title, f"Title mismatch: Expected '{expected_title}"
    driver.find_element("xpath", "(//a[contains(text(),'Books')])[1]").click()
    assert "books" in driver.current_url.lower(), "Failed to navigate to Books page"


@pytest.mark.regression
@pytest.mark.smoke
def test_clickComputers(test_verifyURL):
    driver.find_element("xpath", "(//a[contains(text(),'Computers')])[1]").click()
    assert "computers" in driver.current_url.lower(), "Failed to navigate to Computers page"


@pytest.mark.skip
def test_clickElectronics(test_verifyURL):
    driver.find_element("xpath", "(//a[contains(text(),'Electronics')])[1]").click()
    assert "computers" in driver.current_url.lower(), "Failed to navigate to Electronics page"


@pytest.mark.smoke
def test_clickJewelry(test_verifyURL):
    driver.find_element("xpath", "(//a[contains(text(),'Jewelry')])[1]").click()
    assert "jewelry" in driver.current_url.lower(), "Failed to navigate to Jewelry page"

# @pytest.mark.skip("skipping")
