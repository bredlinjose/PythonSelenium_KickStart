import allure
import pytest
from selenium.webdriver.common.by import By

from page_object_model.generic_utils import common_utils
from page_object_model.pages.home_page import HomePage


@pytest.mark.usefixtures("setup_and_teardown", "screenshot_on_failure")
@allure.severity(allure.severity_level.CRITICAL)
class TestRegister:
    def test_register_with_valid_data(self):
        home_page = HomePage(self.driver)

        # home_page.click_on_my_account_dropdown()
        # register_page = home_page.click_on_register_option()

        register_page = home_page.navigate_to_register_page()

        register_page.set_value_on_firstname_textfield(common_utils.random_string(5))
        register_page.set_value_on_lastname_textfield(common_utils.random_string(4))
        register_page.set_value_on_email_textfield(common_utils.random_email("@yahoo.com"))
        register_page.set_value_on_telephone_textfield(common_utils.random_number(10))
        register_page.set_value_on_password_textfield("Password@123")
        register_page.set_value_on_confirm_password_textfield("")
        register_page.click_on_subscribe_radiobutton("No")
        register_page.click_on_policy_checkbox()
        register_page.click_on_continue_button()

    def test_register_with_invalid_data(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_dropdown()
        register_page = home_page.click_on_register_option()
        register_page.set_value_on_firstname_textfield("")
        register_page.set_value_on_lastname_textfield("")
        register_page.set_value_on_email_textfield("")
        register_page.set_value_on_telephone_textfield("")
        register_page.set_value_on_password_textfield("")
        register_page.set_value_on_confirm_password_textfield("")
        register_page.click_on_subscribe_radiobutton("No")
        register_page.click_on_continue_button()
        assert register_page.verify_warning_is_displayed()
        expected_txt = "Warning: You must agree to the Privacy Policy!"
        actual_txt = register_page.get_warning_text()
        assert actual_txt.__eq__(expected_txt)
