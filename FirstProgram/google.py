from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
title = driver.title
print('Title:', title)

driver.find_element(By.NAME, 'q').send_keys('Bredlin' + Keys.ENTER)
url = driver.current_url
print('URL:', url)
driver.close()
