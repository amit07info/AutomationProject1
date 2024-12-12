import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service('C:\\Users\\amitd.sharma_infobea\\PythonConfiguration\\chromedriver.exe')
driver = webdriver.Chrome(options=options,service=s)


driver.implicitly_wait(5)
driver.get("https://toolsqa.com/")
driver.maximize_window()
driver.find_element("link text","DEMO SITE").click()
main_window_handle = driver.current_window_handle
all_window_handles = driver.window_handles
new_tab_handle = [handle for handle in all_window_handles if handle != main_window_handle][0]
driver.switch_to.window(new_tab_handle)
driver.find_element("xpath","//img[@class='banner-image']").click()
all_window_handles = driver.window_handles
current_window_handle = driver.current_window_handle
new_tab_handle = [handle for handle in all_window_handles if handle != current_window_handle and handle != main_window_handle][0]
driver.switch_to.window(new_tab_handle)
print(f"Switched to new tab: {driver.title}")
driver.find_element(By.XPATH, "//a[contains(text(),'Go To Registration')]").click()
driver.find_element("xpath","//input[@id='first-name']/..//input[@type='text']").send_keys('Amit')
driver.find_element("xpath","//input[@id='last-name']/..//input[@type='text']").send_keys('Sharma')
driver.find_element("xpath","//input[@id='email']/..//input[@type='email']").send_keys('Sharma007@gmail.com')
driver.find_element("xpath","//input[@id='mobile']/..//input[@type='text']").send_keys('1234567890')
select=driver.find_element("id", "country")
S1=Select(select)
S1.select_by_value('4')
driver.find_element("xpath","//input[@id='city']/..//input[@type='text']").send_keys('Indore')
driver.find_element("id","message").send_keys('Python Training')
driver.find_element("xpath","//button[@class='btn btn-block btn-primary']").click()




# Get all window handles (including the main window and the new tab
# Find the handle of the new tab (excluding the main window handle)
# Switch to the new tab
# driver.switch_to.window(new_tab_handle)
# Perform actions in the new tab (e.g., print its title)
# print(f"Switched to new tab: {driver.title}")
# Switch back to the main window
# driver.switch_to.window