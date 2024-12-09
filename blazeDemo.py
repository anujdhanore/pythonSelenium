import time

import allure
import pytest
from allure_commons.types import AttachmentType
from distlib.resources import finder
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

@pytest.fixture()
def test_start_up():
    global driver

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service("C:\\Users\\anuj.dhanore_infobea\\Downloads\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=s)
    driver.implicitly_wait(5)
    driver.get("https://blazedemo.com/")
    driver.maximize_window()

@allure.feature("Testing allure")
def test_select_destination(test_start_up):
    print("Title of the page: ",driver.title)
    header = driver.find_element("tag name","h1")
    print("Header text: ", header.text)
    para1 = driver.find_element("xpath","//div[@class='jumbotron']//div/p[1]")
    para2 = driver.find_element("xpath","//div[@class='jumbotron']//p[2]")
    print("Paragraph 1 : ", para1.text, "\nParagraph 2 : ", para2.text)

    from_port_heading = driver.find_element("xpath", "//h2[text()='Choose your departure city:']")
    print(from_port_heading.text)

    from_port = driver.find_element("name","fromPort")
    sel = Select(from_port)
    sel.select_by_index(1)
    print(sel.options[1].text)

    to_port_heading = driver.find_element("xpath","//h2[contains(text(),'destination city')]")
    print(to_port_heading.text)

    to_port = driver.find_element("name","toPort")
    sel1 = Select(to_port)
    sel1.select_by_index(2)
    print(sel1.options[2].text)

    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

@allure.story("story")
def test_select_flight():
    driver.find_element("xpath","//input[@value='Find Flights']").click()

    flight_list_heading = driver.find_element("xpath","//h3")
    print(flight_list_heading.text)

    flight_lbl = driver.find_element("xpath","//table/thead/tr/th[2]")
    airline_lbl = driver.find_element("xpath","//table/thead/tr/th[3]")
    departs_lbl = driver.find_element("xpath","//table/thead/tr/th[4]")
    arrives_lbl = driver.find_element("xpath","//table/thead/tr/th[5]")
    price_lbl = driver.find_element("xpath","//table/thead/tr/th[6]")

    flight_name = driver.find_element("xpath","//table/tbody/tr[2]/td[2]")
    airline_name = driver.find_element("xpath","//table/tbody/tr[2]/td[3]")
    departs_name = driver.find_element("xpath","//table/tbody/tr[2]/td[4]")
    arrives_name = driver.find_element("xpath","//table/tbody/tr[2]/td[5]")
    flight_price = driver.find_element("xpath","//table/tbody/tr[2]/td[6]")

    print("Selected flight details : ")
    print(flight_lbl.text,airline_lbl.text, departs_lbl.text,arrives_lbl.text, price_lbl.text)
    print(flight_name.text, airline_name.text,departs_name.text,arrives_name.text,flight_price.text)

    choose_flight = driver.find_element("xpath","//table/tbody/tr[2]//input")
    choose_flight.click()

def test_enter_details():
    print(driver.find_element("xpath","//div[@class='container']/h2").text)
    print(driver.find_element("xpath","//div[@class='container']/p[1]").text)
    print(driver.find_element("xpath","//div[@class='container']/p[2]").text)
    print(driver.find_element("xpath","//div[@class='container']/p[3]").text)
    print(driver.find_element("xpath","//div[@class='container']/p[4]").text)
    print(driver.find_element("xpath","//div[@class='container']/p[5]").text)

    driver.find_element("id","inputName").send_keys("Test user")
    driver.find_element("id","address").send_keys("123 street, Richmond")
    driver.find_element("id","city").send_keys("Richmond")
    driver.find_element("id","state").send_keys("Rhode Island")
    driver.find_element("id","zipCode").send_keys("02812")

    card = driver.find_element("name","cardType")
    sel2 = Select(card)
    sel2.select_by_visible_text("American Express")

    driver.find_element("id","creditCardNumber").send_keys("2345 6789 1234 0987")
    driver.find_element("id","creditCardMonth").send_keys("11")
    driver.find_element("name","creditCardYear").send_keys("2026")
    driver.find_element("name","nameOnCard").send_keys("Test user")
    driver.find_element("id","rememberMe").click()
    driver.find_element("xpath","//input[@value='Purchase Flight']").click()

def test_purchase_confirm():
    purchase_confirm = driver.find_element("xpath","//h1")
    print(purchase_confirm.text)
    purchase_details = driver.find_element("xpath", "//table[@class='table']/tbody")
    print(purchase_details.text)

