import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service("C:\\Users\\anuj.dhanore_infobea\\Downloads\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=s)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
time.sleep(4)
print(driver.title)
print(driver.current_url)
comp = driver.find_element("xpath", "//ul[@class='top-menu']/li[2]/a")
a = ActionChains(driver)
a.move_to_element(comp).perform()
a.context_click(comp).perform()

driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
time.sleep(4)

iframe= driver.find_element(By.XPATH,"//iframe[@class='demo-frame lazyloaded']")
driver.switch_to.frame(iframe)

elementsource = driver.find_element("xpath", "//ul[@id='gallery']/li/img[@alt='The peaks of High Tatras']")
elementtarget = driver.find_element("xpath", "//div[@id='trash']")

a.drag_and_drop(elementsource, elementtarget).perform()

driver.switch_to.default_content()

driver.get("https://demo.guru99.com/test/simple_context_menu.html")
doubleclick = driver.find_element("xpath", "//button[@ondblclick='myFunction()']")
a.double_click(doubleclick).perform()
alert = Alert(driver)
print(alert.text)
alert.accept()
#alert.dismiss()

"""driver.find_element("link text","Log in").click()

driver.find_element("id","Email").send_keys("anuj.dhanore@infobeans.com")
driver.find_element("id","Password").send_keys("Test@1234")
driver.find_element("xpath","//input[@value='Log in']").click()
"""
"""
driver.find_element("xpath","//a[text()='Register']").click()
driver.find_element("id","gender-male").click()

driver.find_element("id","FirstName").send_keys("Anuj")
driver.find_element("id","LastName").send_keys("Dhanore")
driver.find_element("id","Email").send_keys("anuj.dhanore+2@infobeans.com")
driver.find_element("id","Password").send_keys("Test@1234")
driver.find_element("id","ConfirmPassword").send_keys("Test@1234")

driver.find_element("name","register-button").click()
driver.find_element("xpath","//input[@value='Continue']").click()"""

"""driver.find_element("link text","Computers").click()
com = driver.find_element("partial link text","Noteb")
print(com.text)
print(com.tag_name)
com.click()
driver.find_element("xpath","//input[@value='Add to cart']").click()
shop = driver.find_element("partial link text","Shopping cart")
print(shop.text)
print(shop.tag_name)
shop.click()"""
