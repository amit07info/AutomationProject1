import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service('C:\\Users\\amitd.sharma_infobea\\PythonConfiguration\\chromedriver.exe')
driver = webdriver.Chrome(options=options,service=s)
driver.implicitly_wait(3)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
# Locator in Selenium
# time.sleep(4)
driver.find_element("name", "username").send_keys("Admin")
driver.find_element("name", "password").send_keys("admin123")
driver.find_element("xpath", "//button[@type='submit']").click()
# time.sleep(4)
# driver.find_element("xpath", "//span='Admin']").click()



