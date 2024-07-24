# wait commands
# switch between windows
# action chains

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
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

currentHandle = driver.current_window_handle
driver.find_element(By.XPATH, "//a[text()= 'OrangeHRM, Inc']").click()
handles = driver.window_handles
for handle in handles:
    if handle != currentHandle:
        driver.switch_to.window(handle)
        break

wait.until(expected_conditions.title_contains('Human Resource'))
facebookLnk = driver.find_element(By.XPATH, "//img[@alt='facebook logo']/..")
act = ActionChains(driver)
act.move_to_element(facebookLnk).click().perform()

driver.close()

handles = driver.window_handles
for handle in handles:
    if handle != currentHandle:
        driver.switch_to.window(handle)
        break

wait.until(expected_conditions.url_contains('facebook'))
title = driver.title
print(title)

driver.quit()
