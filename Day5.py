import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service('C:\\Users\\amitd.sharma_infobea\\PythonConfiguration\\chromedriver.exe')
driver = webdriver.Chrome(options=options,service=s)
# --------------------------------------------------------------------------------------------
# Synchronization:
# implicitly_wait
driver.implicitly_wait(3)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.find_element("name", "username").send_keys("Admin")
driver.find_element("name", "password").send_keys("admin123")
driver.find_element("xpath", "//button[@type='submit']").click()
# Expicit_wait:
# clickable_element = WebDriverWait(driver, 10)
# clickable_element.until(EC.title_contains("OrangeM"))
# print("Action not Completed")
# clickable_element.until(
# EC.frame_to_be_available_and_switch_to_it(("xpath", "//iframe[@id='frm']")))
# clickable_element.until(EC.alert_is_present())
# driver.find_element("id","mn").send_keys("M")
# driver.switch_to.default_content()
# driver.switch_to.parent_frame()
# driver.find_element("id","ln").send_keys("n")
try:
    clickable_element.until(EC.title_contains("OrangeM"))
    print("Action not Completed")
except:
    print("Action not Completed")
finally:
    print("Code Completed")



