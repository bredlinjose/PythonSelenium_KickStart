import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")

driver.find_element(By.LINK_TEXT, "Register").send_keys(Keys.CONTROL+Keys.ENTER)

time.sleep(6)

driver.quit()
