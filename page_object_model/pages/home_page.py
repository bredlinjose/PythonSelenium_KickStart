import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from page_object_model.generic_utils.web_utils import WebUtils
from page_object_model.pages.login_page import LoginPage
from page_object_model.pages.register_page import RegisterPage
from page_object_model.pages.search_page import SearchPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    search_tb = (By.NAME, "search")
    search_icn = (By.XPATH, "//button[contains(@class, 'btn-default')]")
    myAccount_dd = (By.LINK_TEXT, "My Account")
    register_opt = (By.XPATH, "//li/a[text()='Register']")
    login_opt = (By.XPATH, "//li/a[text()='Login']")

    # def set_value_on_search_textfield(self, value):
    #     WebUtils.set_value_to_textfield(*self.search_tb, value)
    #
    # def click_on_search_icon(self):
    #     WebUtils.click_on_element(HomePage.search_icn)

    # def set_value_on_search_textfield(self, value):
    #     self.driver.find_element(*self.search_tb).click()
    #     self.driver.find_element(*self.search_tb).clear()
    #     self.driver.find_element(*self.search_tb).send_keys(value)
    #
    # def click_on_search_icon(self):
    #     self.driver.find_element(*self.search_icn).click()
    #     return SearchPage(self.driver)

    def search_product(self, value):
        self.set_value_on_search_textfield(value)
        return self.click_on_search_icon()

    def click_on_my_account_dropdown(self):
        self.driver.find_element(*self.myAccount_dd).click()

    def click_on_register_option(self):
        self.driver.find_element(*self.register_opt).click()
        return RegisterPage(self.driver)

    def click_on_login_option(self):
        self.driver.find_element(*self.login_opt).click()
        return LoginPage(self.driver)

    def navigate_to_register_page(self):
        self.click_on_my_account_dropdown()
        return self.click_on_register_option()

    def navigate_to_login_page(self):
        self.click_on_my_account_dropdown()
        return self.click_on_login_option()
