from selenium.webdriver.common.by import By

from page_object_model.pages.account_success_page import SuccessPage


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    firstname_tb = (By.ID, "input-firstname")
    lastname_tb = (By.ID, "input-lastname")
    email_tb = (By.ID, "input-email")
    telephone_tb = (By.ID, "input-telephone")
    password_tb = (By.ID, "input-password")
    confirmPassword_tb = (By.ID, "input-confirm")
    policy_cb = (By.NAME, "agree")
    continue_btn = (By.XPATH, "//input[@value = 'Continue']")
    warning_txt = (By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")

    def subscribe_rb(self, value):
        return self.driver.find_element(By.XPATH, f"//label[.='Subscribe']/../div/label[normalize-space()='{value}']")

    def set_value_on_firstname_textfield(self, value):
        self.driver.find_element(*self.firstname_tb).click()
        self.driver.find_element(*self.firstname_tb).clear()
        self.driver.find_element(*self.firstname_tb).send_keys(value)

    def set_value_on_lastname_textfield(self, value):
        self.driver.find_element(*self.lastname_tb).click()
        self.driver.find_element(*self.lastname_tb).clear()
        self.driver.find_element(*self.lastname_tb).send_keys(value)

    def set_value_on_email_textfield(self, value):
        self.driver.find_element(*self.email_tb).click()
        self.driver.find_element(*self.email_tb).clear()
        self.driver.find_element(*self.email_tb).send_keys(value)

    def set_value_on_telephone_textfield(self, value):
        self.driver.find_element(*self.telephone_tb).click()
        self.driver.find_element(*self.telephone_tb).clear()
        self.driver.find_element(*self.telephone_tb).send_keys(value)

    def set_value_on_password_textfield(self, value):
        self.driver.find_element(*self.password_tb).click()
        self.driver.find_element(*self.password_tb).clear()
        self.driver.find_element(*self.password_tb).send_keys(value)

    def set_value_on_confirm_password_textfield(self, value):
        self.driver.find_element(*self.confirmPassword_tb).click()
        self.driver.find_element(*self.confirmPassword_tb).clear()
        self.driver.find_element(*self.confirmPassword_tb).send_keys(value)

    def click_on_policy_checkbox(self):
        self.driver.find_element(*self.policy_cb).click()

    def click_on_continue_button(self):
        self.driver.find_element(*self.continue_btn).click()
        return SuccessPage(self.driver)

    def click_on_subscribe_radiobutton(self, value):
        self.subscribe_rb(value).click()

    def verify_warning_is_displayed(self):
        return self.driver.find_element(*self.warning_txt).is_displayed()

    def get_warning_text(self):
        return self.driver.find_element(*self.warning_txt).text

