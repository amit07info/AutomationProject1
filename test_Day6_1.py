import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

from webdriver_manager.chrome import ChromeDriverManager
import pytest
import allure
@pytest.fixture
@allure.feature("Test")

def test_verifyURL():
    global driver

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service('C:\\Users\\amitd.sharma_infobea\\PythonConfiguration\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=s)
    driver.implicitly_wait(5)
    driver.get("https://blazedemo.com/")
    driver.maximize_window()
    h1=driver.find_element("xpath", "//h1")

    print(h1.text)
    # time.sleep(1)

def test_country(test_verifyURL):
    select=driver.find_element("name", "fromPort")
    S1=Select(select)

    S1.select_by_value("Boston")
    select=driver.find_element("name", "toPort")
    S2=Select(select)
    S2.select_by_visible_text("Rome")
    driver.find_element("xpath", "//input[@type='submit']").click()

def test_bookflight():
    driver.find_element("xpath", "//form[@name='VA43']/..//input[@type='submit']").click()

def test_detail():
    driver.find_element("xpath","//input[@id='inputName']/..//input[@type='text']").send_keys('Amit Sharma')
    driver.find_element("xpath","//input[@id='address']/..//input[@type='text']").send_keys('123 Main St.')
    driver.find_element("xpath","//input[@id='city']/..//input[@type='text']").send_keys('Boston')
    driver.find_element("xpath","//input[@id='state']/..//input[@type='text']").send_keys('United States of America')
    driver.find_element("xpath","//input[@id='zipCode']/..//input[@type='text']").send_keys('10001')

    select=driver.find_element("xpath", "//select[@name='cardType']")
    S3=Select(select)
    S3.select_by_visible_text('American Express')
    driver.find_element("xpath","//input[@id='creditCardNumber']/..//input[@type='text']").send_keys('700000')
    driver.find_element("xpath","//input[@id='nameOnCard']/..//input[@type='text']").send_keys('Amit Sharma')
    driver.find_element("id","rememberMe").click()
    driver.find_element("xpath","//input[@type='submit']").click()




