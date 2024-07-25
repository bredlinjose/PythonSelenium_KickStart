import os
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import Excel_Utils

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

act = ActionChains(driver)
act.scroll_by_amount(200, 450).perform()

file = os.path.abspath('..') + '\\files' + "\\test_data.xlsx"
sheetName = "calculate"
rows = Excel_Utils.get_row_count(file, sheetName)

for r in range(2, rows+1):
    # reading data from excel
    prin = Excel_Utils.read_data(file, sheetName, r, 1)
    interest = Excel_Utils.read_data(file, sheetName, r, 2)
    period = Excel_Utils.read_data(file, sheetName, r, 3)
    perDur = Excel_Utils.read_data(file, sheetName, r, 4)
    fre = Excel_Utils.read_data(file, sheetName, r, 5)
    exp_matVal = Excel_Utils.read_data(file, sheetName, r, 6)

    # passing data to the application
    driver.find_element(By.ID, "principal").send_keys(prin)
    driver.find_element(By.ID, "interest").send_keys(interest)
    driver.find_element(By.ID, "tenure").send_keys(period)
    periodDD = Select(driver.find_element(By.ID, "tenurePeriod"))
    periodDD.select_by_visible_text(perDur)
    frequencyDD = Select(driver.find_element(By.ID, "frequency"))
    frequencyDD.select_by_visible_text(fre)
    calculateBtn = driver.find_element(By.XPATH, "//form[@id='fdMatVal']/descendant::img[contains(@src,'btn_calcutate')]/parent::a")
    driver.execute_script("arguments[0].click();", calculateBtn)
    act_matVal = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

    # validation
    if float(exp_matVal) == float(act_matVal):
        print("test passed")
        # write data in the excel
        Excel_Utils.write_data(file, sheetName, r, 8, "Passed")
        Excel_Utils.fill_green_colour(file, sheetName, r, 8)
    else:
        print("test failed")
        # write data in the excel
        Excel_Utils.write_data(file, sheetName, r, 8, "Failed")
        Excel_Utils.fill_red_colour(file, sheetName, r, 8)

    clearBtn = driver.find_element(By.XPATH, "//form[@id='fdMatVal']/descendant::img[contains(@src,'btn_clear')]/parent::a")
    driver.execute_script("arguments[0].click();", clearBtn)
    time.sleep(2)

driver.quit()