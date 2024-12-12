import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

from webdriver_manager.chrome import ChromeDriverManager


#Assert:
@pytest.fixture
def test_verifyURL():
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service('C:\\Users\\amitd.sharma_infobea\\PythonConfiguration\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=s)
    driver.implicitly_wait(5)
    driver.get("https://demowebshop.tricentis.com")
    driver.maximize_window()

def test_ClickBooks(test_verifyURL):
    expected_title = "Demo Web Shop"
    actual_title = driver.title
    # Assert that the actual title macthes the expected title
    assert actual_title == expected_title, f"Title mismatch: Expected '{expected_title}"
    driver.find_element("xpath", "(//a[contains(text(),'Books')])[1]").click()
    assert "books" in driver.current_url.lower(), "Failed to navigate to Books page"



