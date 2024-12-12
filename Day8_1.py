import json
import time
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Fixture to set up WebDriver
@pytest.fixture(scope="function")  # Ensures that the driver is created for each test function
def driver1():
    global driver
    # Set up WebDriver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service = Service("C:\\Users\\amitd.sharma_infobea\\PythonConfiguration\\chromedriver.exe")  # Update the path to your chromedriver
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()


    # Cleanup code: Quit the driver after the test

# Fixture to load data from the YAML file
'''
@pytest.fixture(scope="session")
def config_data():
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)  # Returns the content as a dictionary
'''
@pytest.fixture(scope="session")
def config_data():
    with open("config.json", "r") as file:
        return json.load(file)  # Returns the content as a dictionary

def test_example(driver1, config_data):
    # Use data from the YAML configuration
    url = config_data["url"]
    username = config_data["username"]
    password = config_data["password"]

    # Open the URL
    driver.get(url)
    time.sleep(4)

    # Test steps
    driver.find_element("name", "username").send_keys(username)
    driver.find_element("name", "password").send_keys(password)
    driver.find_element("xpath", "//button[@type='submit']").click()


