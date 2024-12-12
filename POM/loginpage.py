# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#
#     # Locators for elements on the page
#     username_field = (By.XPATH, "//input[@placeholder='Username']")
#     password_field = (By.XPATH, "//input[@placeholder='Password']")
#     login_button = (By.XPATH, "//button[@type='submit']")
#     #error_message = (By.ID, "spanMessage")
#
#     # Actions or Methods to interact with elements on the page
#     def enter_username(self, username):
#         self.driver.find_element(*self.username_field).send_keys(username)
#
#     def enter_password(self, password):
#         self.driver.find_element(*self.password_field).send_keys(password)
#
#     def click_login_button(self):
#         self.driver.find_element(*self.login_button).click()
#
#
#     def login(self, username, password):
#         self.enter_username(username)
#         self.enter_password(password)
#         self.click_login_button()
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Private Locators for elements on the page
    _username_field = (By.XPATH, "//input[@placeholder='Username']")
    _password_field = (By.XPATH, "//input[@placeholder='Password']")
    _login_button = (By.XPATH, "//button[@type='submit']")
    _error_message = (By.ID, "spanMessage")

    # Actions or Methods to interact with elements on the page
    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self._username_field))
        self.driver.find_element(*self._username_field).clear()
        self.driver.find_element(*self._username_field).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self._password_field))
        self.driver.find_element(*self._password_field).clear()
        self.driver.find_element(*self._password_field).send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self._login_button))
        self.driver.find_element(*self._login_button).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def get_error_message(self):
        try:
            error_message = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self._error_message))
            return error_message.text
        except:
            return None