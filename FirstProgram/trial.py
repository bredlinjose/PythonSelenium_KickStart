import os
import time

from selenium import webdriver
from selenium.common import ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

uploadPath = os.path.dirname(os.path.abspath('.')) + '\\files\\dummy.png'
downloadPath = os.path.dirname(os.path.abspath('.')) + '\\files'
print(uploadPath)
print(downloadPath)

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {"download.default_directory": downloadPath})
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://selectorshub.com/')
wait = WebDriverWait(driver, 15)
wait.until(expected_conditions.url_contains('https://selectorshub.com/'))

practicePageLnk = driver.find_element(By.XPATH, "//a[text()='PracticePage']")
practicePageLnk.click()

wait.until(expected_conditions.url_contains('xpath-practice-page'))
pageTitle = driver.title

act = ActionChains(driver)

chooseFileBtn = driver.find_element(By.ID, "myFile")
chooseFileBtn.send_keys(uploadPath)

downloadLnk = driver.find_element(By.PARTIAL_LINK_TEXT, "Click to Download PNG File")
downloadLnk.click()

time.sleep(10)
