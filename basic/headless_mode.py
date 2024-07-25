
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

ops = webdriver.ChromeOptions()
ops.add_argument("--headless")
driver = webdriver.Chrome(options=ops)
driver.implicitly_wait(10)
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
wait.until(expected_conditions.title_contains('OrangeHRM'))
title = driver.title
print('Title:', title)

driver.find_element(By.NAME, 'username').send_keys('Admin')
driver.find_element(By.NAME, 'password').send_keys('admin123')
driver.find_element(By.XPATH, "//button[@type='submit']").click()

wait.until(expected_conditions.url_contains('dashboard'))
text = driver.find_element(By.XPATH, "//h6").text
print(text)

driver.quit()
