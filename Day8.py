import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import allure
from webdriver_manager.chrome import ChromeDriverManager

#Paramatization:
@pytest.fixture()
# @allure.feature
def test_verifyURL():
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service('C:\\Users\\amitd.sharma_infobea\\PythonConfiguration\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=s)
    driver.implicitly_wait(5)
    driver.get("https://opensource-demo.orangehrmlive.com")
    driver.maximize_window()

# Parameterize test with different usernames and passwords
@pytest.mark.parametrize(
    "username, password",
    [
        ("Admin", "admin123"),       # Valid credentials
        ("invalid_user", "admin123"), # Invalid username
        ("Admin", "wrongpassword"),  # Invalid password
        ("", ""),                    # Empty credentials
    ]
)

def test_login(test_verifyURL, username, password):
    # Locate and interact with username field
    username_field = driver.find_element("name", "username")
    username_field.send_keys(username)

    # Locate and interact with password field
    password_field = driver.find_element("name", "password")
    #password_field.clear()
    password_field.send_keys(password)

    # Click login button
    login_button = driver.find_element("xpath", "//button[@type='submit']")
    login_button.click()