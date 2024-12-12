import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
import pytest
import allure
# pytest.fixture:
@pytest.fixture
# @allure.feature("Test")

def test_verifyURL():
    global driver

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service('C:\\Users\\amitd.sharma_infobea\\PythonConfiguration\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=s)
    driver.implicitly_wait(5)
    driver.get("https://demowebshop.tricentis.com")
    driver.maximize_window()

# pytest -m "smoke or regression"
# pytest -m "regression and login"
# Q. except smoke run all testcases

#1. pytest -m "smoke or regression"

@pytest.mark.smoke
def test_clickBooks(test_verifyURL):
    driver.find_element("xpath", "(//a[contains(text(),'Books')])[1]").click()

@pytest.mark.regression
@pytest.mark.login
def test_clickComputers(test_verifyURL):
    driver.find_element("xpath", "(//a[contains(text(),'Computers')])[1]").click()

# Grouping Feature:




# @pytest.mark.skip("skipping")
# def test_clicklogout():
#     print("this is just sample one")



