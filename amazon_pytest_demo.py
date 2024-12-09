import time
from unittest.result import failfast

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def start_up():
    global driver

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    # s = Service("C:\\Users\\anuj.dhanore_infobea\\Downloads\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=Service(), options=options)
    # driver.get("https://www.softwaretestingmaterial.com/sample-webpage-to-automate/")
    driver.implicitly_wait(5)
    driver.get("https://www.amazon.in/")
    time.sleep(10)
    driver.maximize_window()


@allure.feature("Test buy now")
def test_login(start_up):
    time.sleep(2)
    act = ActionChains(driver)
    signin_popup = driver.find_element("id", "nav-link-accountList-nav-line-1")
    act.move_to_element(signin_popup).perform()

    driver.find_element("xpath", "//div[@id='nav-flyout-ya-signin']/a/span").click()
    driver.find_element("id", "ap_email").send_keys("Username")
    driver.find_element("xpath", "//input[@id='continue']").click()
    driver.find_element("id", "ap_password").send_keys("Password")
    driver.find_element("id", "signInSubmit").click()
    #driver.find_element("id","auth-mfa-otpcode").send_keys()
    time.sleep(10)
    driver.find_element("id", "auth-signin-button").click()


@allure.feature("Test buy now")
def test_search_prod():
    driver.find_element("id", "twotabsearchtextbox").send_keys("iphone")
    search_items = driver.find_elements("xpath",
                                        "//div[@id='nav-flyout-searchAjax']//div[@class='s-suggestion-container']/div[1]")

    for item in search_items:
        item_name = item.text
        if item_name.lower() == "iphone 13 128gb":
            item.click()
            break

    # driver.find_element("xpath","//form[@name='site-search']//input[@type='submit']").click()


@allure.feature("Test buy now")
def test_search_result():
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Results']")))

    result_items = driver.find_elements("xpath",
                                        "//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']/a/span")

    for item in result_items:
        item_name = item.text
        if item_name == "Apple iPhone 13 (128GB) - Blue":
            driver.execute_script("arguments[0].scrollIntoView();", item)
            item.click()
            break

    driver.save_screenshot("C:\\Users\\anuj.dhanore_infobea\\PycharmProjects\\screenShots\\image.png")


@allure.feature("Test buy now")
def test_add_product_to_cart():
    driver.switch_to.window(driver.window_handles[1])
    prod_name = driver.find_element("id", "productTitle")
    print(prod_name.text)

    driver.find_element("css selector", "input[id='buy-now-button']").click()
    assert failfast(test_add_product_to_cart)


@allure.feature("Test buy now")
def test_add_card_details():
    oth_pymt_mthd = driver.find_element("xpath", "//span[contains(text(),'Another payment method')]")
    driver.execute_script("arguments[0].scrollIntoView();", oth_pymt_mthd)

    driver.find_element("xpath", "//input[@value='SelectableAddCreditCard']").click()
    driver.find_element("xpath",
                        "//span[text()='Credit or debit card']/../following-sibling::div[2]//span[@id='apx-add-credit-card-action-test-id']//img[1]").click()

    driver.switch_to.frame("ApxSecureIframe")

    card_no = driver.find_element("xpath", "//input[@name='addCreditCardNumber']")
    card_no.send_keys("4242424242424242")
    nick_name = driver.find_element("css selector", "input[name='ppw-accountHolderName']")
    nick_name.clear()
    nick_name.send_keys("Test user")

    month_pick = driver.find_element("name", "ppw-expirationDate_month")
    sel = Select(month_pick)
    sel.select_by_value("3")
    clk =driver.find_element("xpath","//label[text()='Expiry date']")
    clk.click()

    year_pick = driver.find_element("name", "ppw - expirationDate_year")
    sel = Select(year_pick)
    sel.select_by_value("2026")
    clk.click()

    driver.find_element("name", "ppw-widgetEvent:AddCreditCardEvent").click()

    print(driver.find_element("xpath", "//span[text()='Card number is not correct.']").text)
