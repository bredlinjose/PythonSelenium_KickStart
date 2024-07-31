import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_tutorialsninja():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    expected_title = "Your Store ABC"
    actual_title = driver.title
    assert actual_title.__eq__(expected_title)
    time.sleep(2)
    driver.find_element(By.NAME, "search").send_keys("HP")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[contains(@class, 'btn-default')]").click()
    time.sleep(2)
    assert driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
    time.sleep(5)
    driver.quit()
