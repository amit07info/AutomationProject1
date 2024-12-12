import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from POM.loginpage import LoginPage


@pytest.fixture(scope="module")
def setup():
    # Set up WebDriver (Chrome in this case)
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service('C:\\Users\\amitd.sharma_infobea\\PythonConfiguration\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=s)
    driver.implicitly_wait(5)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()


def test_valid_login(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login_button()
    # Perform valid login
    # login_page.login("Admin", "admin123")
