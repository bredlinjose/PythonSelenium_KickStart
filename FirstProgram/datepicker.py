from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://jqueryui.com/datepicker/")
title = driver.title
print('Title:', title)

date = 25
month = 'December'
year = 2022

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.title_contains("Datepicker"))

frame = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
driver.switch_to.frame(frame)

dateTb = driver.find_element(By.ID, "datepicker")
dateTb.click()


mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

while not (mon == month and int(yr) == year):
    print(mon, month)
    print(yr, year)
    previousIcn = driver.find_element(By.XPATH, "//a[@title='Prev']")
    previousIcn.click()
    # nextIcn = driver.find_element(By.XPATH, "//a[@title='Next']")
    # nextIcn.click()
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text




dateTxt = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/descendant::a")
for ele in dateTxt:
    if ele.text == date:
        ele.click()
        break
