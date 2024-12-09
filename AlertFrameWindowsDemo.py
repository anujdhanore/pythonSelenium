import time
from typing import final

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service("C:\\Users\\anuj.dhanore_infobea\\Downloads\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=s)
driver.implicitly_wait(5)
driver.get("https://toolsqa.com/selenium-training")
driver.maximize_window()

driver.find_element("link text", "DEMO SITE").click()

# Get all window handles (including the main window and the new tab)
main_window_handle = driver.current_window_handle
all_window_handles = driver.window_handles

# Find the handle of the new tab (excluding the main window handle)
new_tab_handle = [handle for handle in all_window_handles if handle != main_window_handle][0]

for handle in all_window_handles:
    if handle != main_window_handle:
        driver.switch_to.window(handle)
        break

# Switch to the new tab
#driver.switch_to.window(new_tab_handle1)

WebDriverWait(driver,10).until(EC.number_of_windows_to_be(2))
print(driver.title)

driver.find_element("xpath", "//img[@src='/images/WB.svg']").click()

driver.switch_to.window(driver.window_handles[-1])
driver.close()
driver.switch_to.window(driver.window_handles[1])

ale = driver.find_element("xpath", "//h5[text()='Alerts, Frame & Windows']")
driver.execute_script("arguments[0].scrollIntoView();", ale)
ale.click()

driver.find_element("xpath", "//span[text()='Alerts']").click()

ele = driver.find_element("id", "javascriptAlertsWrapper")
driver.execute_script("arguments[0].scrollIntoView();", ele)

driver.find_element("css selector", "#alertButton").click()
al = Alert(driver)
print(al.text)
al.accept()
"""
driver.find_element("css selector","#alertButton").click()
time.sleep(6)
print(al.text)
al.accept()

driver.find_element("id","confirmButton").click()
print(al.text)
al.accept()
print(driver.find_element("id","confirmResult").text)

driver.find_element("id","confirmButton").click()
print(al.text)
al.dismiss()
print(driver.find_element("id","confirmResult").text)

driver.find_element("id","promtButton").click()
print(al.text)
al.send_keys("Anuj Dhanore")
al.accept()
print(driver.find_element("id","promptResult").text)
"""
"""
driver.find_element("link text","Nested Frames").click()

#fr_left = driver.find_element("name","frame-left")
driver.switch_to.frame("frame-top")
print("Switched to Top frame")

driver.switch_to.frame("frame-left")
print("Switched to Left frame")

print(driver.find_element("xpath","//body[contains(text(),'LEFT')]").text)

driver.switch_to.parent_frame()
print("Switched to parent")
print(driver.find_element("tag name","html").tag_name)

driver.switch_to.frame("frame-right")
print("Switched to Right frame")
print(driver.find_element("xpath","//body[contains(text(),'RIGHT')]").text)

driver.switch_to.parent_frame()
print("Switched to parent")

driver.switch_to.frame("frame-middle")
print("Switched to Middle frame")
print(driver.find_element("xpath","//div[(text()='MIDDLE')]").text)

driver.switch_to.default_content()

driver.switch_to.frame("frame-bottom")
print(driver.find_element("xpath","//body[contains(text(),'BOTTOM')]").text)"""
