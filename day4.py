import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service("C:\\Users\\anuj.dhanore_infobea\\Downloads\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=s)
# driver.get("https://www.softwaretestingmaterial.com/sample-webpage-to-automate/")
driver.implicitly_wait(5)
driver.get("https://www.amazon.in/")
driver.maximize_window()

driver.find_element("id","twotabsearchtextbox").send_keys("iphone")
driver.find_element("xpath","//form[@name='site-search']//input[@type='submit']").click()

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH,"//h2[text()='Results']")))

ele = driver.find_element("xpath","//span[text()='Apple iPhone 13 (128GB) - Starlight']")
driver.execute_script("arguments[0].scrollIntoView();",ele)
driver.save_screenshot("C:\\Users\\anuj.dhanore_infobea\\PycharmProjects\\screenShots\\image.png")

driver.execute_script("window.scrollBy(0, 500)")
driver.save_screenshot("C:\\Users\\anuj.dhanore_infobea\\PycharmProjects\\screenShots\\image1.png")

