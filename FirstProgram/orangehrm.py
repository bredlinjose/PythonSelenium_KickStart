from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
title = driver.title
print('Title:', title)

driver.find_element(By.NAME, 'username').send_keys('Admin')
driver.find_element(By.NAME, 'password').send_keys('admin123')
driver.find_element(By.XPATH, "//button[@type='submit']").click()

text = driver.find_element(By.XPATH, "//h6").text

if text.__contains__('Dashboard'):
    print('Test Case Passed')
else:
    print('Test Case Failed')

driver.close()
