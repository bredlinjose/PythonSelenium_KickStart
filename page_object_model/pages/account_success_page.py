from selenium import webdriver
from selenium.webdriver.common.by import By


class SuccessPage:
    def __init__(self, driver):
        self.driver = driver

    accountCreated_txt = (By.XPATH, "//div[@id='content']/h1")
    successful_txt = (By.XPATH, "//div[@id='content']/p[contains(.,'Congratulations')]")
    continue_btn = (By.LINK_TEXT, "Continue")

    def get_account_created_text(self):
        return self.driver.find_element(*self.accountCreated_txt).text

    def verify_successful_message_is_displayed(self):
        return self.driver.find_element(*self.successful_txt).is_displayed()

    def click_on_continue_button(self):
        self.driver.find_element(*self.continue_btn).click()
