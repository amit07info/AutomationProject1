import time
import pytest
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import allure

# Fixture to set up WebDriver
@pytest.fixture(scope="function")
@allure.feature
def driver1():
    # Set up WebDriver
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service = Service("C:\\Users\\amitd.sharma_infobea\\PythonConfiguration\\chromedriver.exe")  # Update the path
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver



# Function to fetch test data from the specified CSV file
def get_csv_data(file_path):
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        return [row for row in reader]  # Returns a list of dictionaries


# Test using data from CSV
def test_example(driver1):
    # Specify the path to your CSV file
    csv_file_path = r"C:\Users\amitd.sharma_infobea\PycharmProjects\AutomationProject1\config.csv"

    # Fetch test data from the CSV file
    test_data_list = get_csv_data(csv_file_path)

    for test_data in test_data_list:
        url = test_data["url"]
        username = test_data["username"]
        password = test_data["password"]

        # Open the URL
        driver.get(url)
        time.sleep(2)

        # Test steps
        driver.find_element("name", "username").send_keys(username)
        driver.find_element("name", "password").send_keys(password)
        login_button = driver.find_element("xpath", "//button[@type='submit']")
        login_button.click()

        # Navigate back to reset for the next test case
        # driver.back()
        # time.sleep(2)


# url	username	password
# https://opensource-demo.orangehrmlive.com/web/index.php/auth/login	Admin	admin123
# https://opensource-demo.orangehrmlive.com/web/index.php/auth/login	Admin1	admin123
