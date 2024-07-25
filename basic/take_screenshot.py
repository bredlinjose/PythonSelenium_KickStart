import time
import os

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")

driver.get_screenshot_as_file(os.path.dirname(os.path.abspath('.')) + '\\files\\screenshot' + "\\screenshot1.png")
driver.save_screenshot(os.path.dirname(os.path.abspath('.')) + '\\files\\screenshot' + "\\screenshot.png")

# driver.get_screenshot_as_png()  # driver.get_screenshot_as_base64()  # saves in binary format

time.sleep(6)

driver.quit()
