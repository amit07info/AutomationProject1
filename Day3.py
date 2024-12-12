import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service('C:\\Users\\amitd.sharma_infobea\\PythonConfiguration\\chromedriver.exe')
driver = webdriver.Chrome(options=options,service=s)

driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
driver.maximize_window()
time.sleep(4)
iframe= driver.find_element(By.XPATH,"//iframe[@class='demo-frame lazyloaded']")
driver.switch_to.frame(iframe)
elementsource = driver.find_element("xpath", "//ul[@id='gallery']/li/img[@alt='The peaks of High Tatras']")
elementtarget = driver.find_element("xpath", "//div[@id='trash']")
a = ActionChains(driver)
a.drag_and_drop(elementsource, elementtarget).perform()

driver.switch_to.default_content()