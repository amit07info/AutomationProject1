from behave import *

import time
import csv
import logging
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
from selenium.webdriver.common.by import By

#Report html (demo web shop):::

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

@given(u'open demowebshop browser')
def step_impl(context):
    global driver
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_experimental_option("detach", True)
    s = Service("C:\\Users\\amitd.sharma_infobea\\PythonConfiguration\\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=s)
    driver.get("https://demowebshop.tricentis.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()

@when(u'Navigate to Registration page and Fill all the mendatory details and click register')
def step_impl(context):
    driver.find_element("xpath", "(//a[contains(text(),'Register')])").click()
    driver.find_element("xpath","//input[@id='gender-male']").click()
    driver.find_element("xpath", "//input[@id='FirstName']/..//input[@type='text']").send_keys('Amit')
    driver.find_element("xpath", "//input[@id='LastName']/..//input[@type='text']").send_keys('Sharma')
    driver.find_element("xpath", "//input[@id='Email']/..//input[@type='text']").send_keys('amitsharma7@gmail.com')
    driver.find_element("xpath", "//input[@id='Password']/..//input[@type='password']").send_keys('admin123')
    driver.find_element("xpath", "//input[@id='ConfirmPassword']/..//input[@type='password']").send_keys('admin123')
    driver.find_element("xpath","//input[@id='register-button']").click()

@then(u'enter valid credential Email "amitsharma7@hmail.com" and password "admin123"')
def step_impl(context):
    driver.find_element("xpath", "//input[@id='Email']/..//input[@type='text']").send_keys('amitsharma7@gmail.com')
    driver.find_element("xpath", "//input[@id='Password']/..//input[@type='password']").send_keys('admin123')
    driver.find_element("xpath", "//input[@value='Log in']/..//input[@type='submit']").click()

@then(u'click on Computer and click to Notebooks')
def step_impl(context):
    driver.find_element("xpath", "(//a[contains(text(),'Computers')])").click()
    driver.find_element("xpath", "(//a[contains(text(),'Notebooks')])").click()

@then(u'click on Add to Cart')
def step_impl(context):
    driver.find_element("xpath", "//input[@value='Add to cart']/..//input[@type='button']").click()

@then(u'Go to Shopping Cart and click on Check out')
def step_impl(context):
    driver.find_element("xpath", "//input[@value='Shopping cart']/..//input[@type='submit']").click()
    driver.find_element("id", "termsofservice").click()
    driver.find_element("id", "checkout").click()