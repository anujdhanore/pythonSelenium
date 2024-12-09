import time
from sys import exception

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
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

"""dd = driver.find_element("name", "dropdown")
sel = Select(dd)
sel.select_by_index(3)

mdd = driver.find_element("name", "multipleselect[]")
sel = Select(mdd)
sel.select_by_index(1)
sel.select_by_index(2)

sel.deselect_all()"""

uname = driver.find_element(By.CSS_SELECTOR,"input[name='username']")
uname.send_keys("Admin")
pwd = driver.find_element("css selector", "input[name='password']")
pwd.send_keys("admin123")
lgnbtn = driver.find_element("css selector",".orangehrm-login-button")
lgnbtn.click()

try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_contains("OrangeM"))

except Exception as e:
    print("Wait not working", e)

