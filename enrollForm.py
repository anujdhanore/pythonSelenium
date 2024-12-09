import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service("C:\\Users\\anuj.dhanore_infobea\\Downloads\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=s)
driver.implicitly_wait(5)
driver.get("https://toolsqa.com/selenium-training")
driver.maximize_window()

tutorial = driver.find_element("css selector","a.navbar__tutorial-menu")
tutorial.click()
hovering = driver.find_element("xpath","//span[text()='QA Practices']")
act =ActionChains(driver)
act.move_to_element(hovering).perform()
tutorial.click()

act.scroll_to_element(driver.find_element("xpath","//u[text()='Paid Training']"))

driver.find_element("id","first-name").send_keys("First")
driver.find_element("name","lastName").send_keys("Last")
driver.find_element("id","email").send_keys("first.last@gmail.com")
driver.find_element("name","mobile").send_keys("5678954321")

country = driver.find_element("id","country")
sel = Select(country)
sel.select_by_visible_text("India")

driver.find_element("id","city").send_keys("Indore")
driver.find_element("id","message").send_keys("Test data provided")
driver.find_element("css selector",".btn.btn-block.btn-primary").click()