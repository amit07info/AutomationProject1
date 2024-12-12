import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_experimental_option("detach", True)
s = Service('C:\\Users\\amitd.sharma_infobea\\PythonConfiguration\\chromedriver.exe')
driver = webdriver.Chrome(options=options,service=s)

driver.get("https://blazedemo.com/")
driver.maximize_window()
time.sleep(4)
h1=driver.find_element("xpath", "//h1")
# by- is the locator and after its value
print(h1.text)
time.sleep(1)
# <select name="fromPort" class="form-inline"> (In this select is the header and under this there are two attributes name and class)
select=driver.find_element("name", "fromPort")
S1=Select(select)
# because to handle dropdown to select option. and S1 is the object.
# 3methods to select- indexing, by text, by value.
S1.select_by_value("Boston")
select=driver.find_element("name", "toPort")
S2=Select(select)
S2.select_by_visible_text("Rome")
driver.find_element("xpath", "//input[@type='submit']").click()
driver.find_element("xpath", "//form[@name='VA43']/..//input[@type='submit']").click()
time.sleep(1)
driver.find_element("xpath","//input[@id='inputName']/..//input[@type='text']").send_keys('Amit Sharma')
time.sleep(1)
driver.find_element("xpath","//input[@id='address']/..//input[@type='text']").send_keys('123 Main St.')
time.sleep(1)
driver.find_element("xpath","//input[@id='city']/..//input[@type='text']").send_keys('Boston')
time.sleep(1)
driver.find_element("xpath","//input[@id='state']/..//input[@type='text']").send_keys('United States of America')
time.sleep(1)
driver.find_element("xpath","//input[@id='zipCode']/..//input[@type='text']").send_keys('10001')
# select=driver.find_element("xpath","//select[@id='cardType']/..//option[@value='amex']")
select=driver.find_element("xpath", "//select[@name='cardType']")
S3=Select(select)
S3.select_by_visible_text('American Express')
driver.find_element("xpath","//input[@id='creditCardNumber']/..//input[@type='text']").send_keys('700000')
driver.find_element("xpath","//input[@id='nameOnCard']/..//input[@type='text']").send_keys('Amit Sharma')
driver.find_element("id","rememberMe").click()
driver.find_element("xpath","//input[@type='submit']").click()


