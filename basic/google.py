from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
title = driver.title
print('Title:', title)

wait = WebDriverWait(driver, 10)

searchTb = wait.until(expected_conditions.presence_of_element_located((By.NAME, 'q')))

searchTb.send_keys('Bredlin' + Keys.ENTER)

url = driver.current_url
print('URL:', url)
driver.close()
