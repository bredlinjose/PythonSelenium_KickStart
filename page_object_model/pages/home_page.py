import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from page_object_model.generic_utils.web_utils import WebUtils

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    search_tb = (By.NAME, "search")
    search_icn = (By.XPATH, "//button[contains(@class, 'btn-default')]")
    myaccount_dd = (By.LINK_TEXT, "My Account")
    register_opt = (By.XPATH, "//li/a[text()='Register']")
    login_opt = (By.XPATH, "//li/a[text()='Login']")

    def set_value_on_search_textfield(self, value):
        WebUtils.set_value_to_textfield(*self.search_tb, value)

    def click_on_search_icon(self):
        WebUtils.click_on_element(HomePage.search_icn)

    # def set_value_on_search_textfield(self, value):
    #     self.driver.find_element(*self.search_tb).click()
    #     self.driver.find_element(*self.search_tb).clear()
    #     self.driver.find_element(*self.search_tb).send_keys(value)
    #
    # def click_on_search_icon(self):
    #     self.driver.find_element(*self.search_icn).click()
    #     time.sleep(10)
