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
year = 2027

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.title_contains("Datepicker"))

frame = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
driver.switch_to.frame(frame)

dateTb = driver.find_element(By.ID, "datepicker")
dateTb.click()


mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
nextIcn = driver.find_element(By.XPATH, "//a[@title='Next']")
previousIcn = driver.find_element(By.XPATH, "//a[@title='Prev']")

# Assuming you have locators for next/previous month and year buttons
next_month_button_locator = (By.XPATH, "//a[@title='Next']")
prev_month_button_locator = (By.XPATH, "//a[@title='Prev']")
next_year_button_locator = (By.XPATH, "//a[@title='Next Year']")
prev_year_button_locator = (By.XPATH, "//a[@title='Previous Year']")

# ... (rest of the code remains the same)

# Handle navigation to target month/year
while displayed_year != year or displayed_month != month:
    if displayed_year < year:
        next_year_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(next_year_button_locator)
        )
        next_year_button.click()
    elif displayed_year > year:
        prev_year_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(prev_year_button_locator)
        )
        prev_year_button.click()

    if displayed_month < month:
        next_month_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(next_month_button_locator)
        )
        next_month_button.click()
    elif displayed_month > month:
        prev_month_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(prev_month_button_locator)
        )
        prev_month_button.click()

dateTxt = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/descendant::a")
for ele in dateTxt:
    if ele.text == date:
        ele.click()
        break
