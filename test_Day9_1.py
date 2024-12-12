import json
import time
import csv

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
from selenium.webdriver.common.by import By

# Login through CSV file------------------
@pytest.fixture()
def params():
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service("C:\\Users\\amitd.sharma_infobea\\PythonConfiguration\\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=s)
    driver.implicitly_wait(10)
    #driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    yield
    driver.close()


# Function to fetch test data from the specified CSV file
def get_csv_data(file_path):
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        return [row for row in reader]  # Returns a list of dictionaries


# Test using data from CSV
    # Parameterize test cases based on CSV data
@pytest.mark.parametrize("test_data", get_csv_data(r"C:\Users\amitd.sharma_infobea\PycharmProjects\AutomationProject1\config.csv"))
def test_example(params, test_data):

         driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Fetch username and password from test data
        username = test_data["username"]
        password = test_data["password"]

        # Open the URL
        time.sleep(2)

        # Test steps
        driver.find_element("name", "username").send_keys(username)
        driver.find_element("name", "password").send_keys(password)

        # Navigate back to reset for the next test case
        # driver.back()
        # time.sleep
