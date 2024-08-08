from selenium import webdriver
from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    product_txt = (By.LINK_TEXT, "HP LP3065")
    noProduct_txt = (By.XPATH, "//div[@id='content']/h2/following-sibling::p")

    def display_valid_product_status(self):
        return self.driver.find_element(*self.product_txt).is_displayed()

    def display_invalid_product_status(self):
        return self.driver.find_element(*self.noProduct_txt).is_displayed()
