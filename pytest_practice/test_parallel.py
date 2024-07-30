import time

from selenium import webdriver


def test_google():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com/")
    time.sleep(2)
    driver.quit()


def test_amazon():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.in/")
    time.sleep(2)
    driver.quit()


def test_flipkart():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.flipkart.com/")
    time.sleep(2)
    driver.quit()


def test_selectorhub():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://selectorshub.com/")
    time.sleep(2)
    driver.quit()


def test_qafox():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.qafox.com/")
    time.sleep(2)
    driver.quit()

#  pytest -n 5 test_parallel.py  --> parallel execution with 5 worker
