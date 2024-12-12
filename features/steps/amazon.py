from _ast import And

from behave import *

import time
import logging
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


@Given(u'open the Amazon browser')
def step_impl(context):
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service('C:\\Users\\amitd.sharma_infobea\\PythonConfiguration\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=s)
    driver.implicitly_wait(20)
    driver.get("https://www.amazon.in/")
    # driver.refresh()
    driver.maximize_window()

    # h1=driver.find_element("xpath", "//h1")
    # print(h1.text)
    time.sleep(10)
    driver.find_element("xpath", "//button[@class='a-button-text']").click()

@When(u'Try Login Successfully')
def step_impl(context):
    # driver.refresh()
    select=driver.find_element("xpath","//span[@id='nav-link-accountList-nav-line-1']").click()
    select=driver.find_element("xpath","//input[@id='ap_email']").send_keys(7000769892)
    select=driver.find_element("xpath", "//span[@id='continue']").click()
    select = driver.find_element("xpath", "//input[@id='ap_password']").send_keys('Sharma@123')
    select = driver.find_element("xpath", "//span[@id='auth-signin-button']").click()

@Then(u'test_searchproduct, test_AddtoCart and test_BuyNow')
def step_impl(context):
    select = driver.find_element("xpath", "//input[@id='twotabsearchtextbox']").send_keys('jackets for men stylish latest')
    select=driver.find_element("id","nav-search-submit-text").click()
    select=select = driver.find_element("xpath", "(//a[@data-type='productTitle'])[1]").click()
    select = driver.find_element("xpath","//span[@id='submit.add-to-cart']").click()
    select = driver.find_element("xpath", "//span[@id='sc-buy-box-ptc-button']").click()
    time.sleep(4)

@Then(u'test_Payment')
def step_impl(context):
    driver.find_element("xpath", "(//input[@type='radio'])[1]").click()
    time.sleep(5)
    driver.find_element("xpath","(//a[@href='#'])[2]").click()
    driver.switch_to.frame("ApxSecureIframe")
    driver.find_element("xpath", "//input[@name='addCreditCardNumber']").send_keys(374245455400126)
    exp_date=driver.find_element("xpath", "//select[@name='ppw-expirationDate_month']")
    sel=Select(exp_date)
    sel.select_by_visible_text('03')
    exp_year = driver.find_element("xpath", "//select[@name='ppw-expirationDate_year']")
    sel = Select(exp_year)
    sel.select_by_visible_text('2026')
    driver.find_element("xpath","//input[@name='ppw-widgetEvent:AddCreditCardEvent']").click()
