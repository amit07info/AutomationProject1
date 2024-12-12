import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_experimental_option("detach", True)
s = Service("C:\\Users\\amitd.sharma_infobea\\PythonConfiguration\\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=s)
driver.get("https://demowebshop.tricentis.com/")
driver.implicitly_wait(10)
driver.maximize_window()


driver.find_element("xpath", "(//a[contains(text(),'Register')])").click()
driver.find_element("xpath","//input[@id='gender-male']").click()
driver.find_element("xpath", "//input[@id='FirstName']/..//input[@type='text']").send_keys('Amit')
driver.find_element("xpath", "//input[@id='LastName']/..//input[@type='text']").send_keys('Sharma')
driver.find_element("xpath", "//input[@id='Email']/..//input[@type='text']").send_keys('amitsharma7@gmail.com')
driver.find_element("xpath", "//input[@id='Password']/..//input[@type='password']").send_keys('admin123')
driver.find_element("xpath", "//input[@id='ConfirmPassword']/..//input[@type='password']").send_keys('admin123')




