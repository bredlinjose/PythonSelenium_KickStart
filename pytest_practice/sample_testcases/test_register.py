import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:
    def test_check_first_and_last_name_functionality(self):
        self.driver.find_element(By.LINK_TEXT, "My Account").click()
        self.driver.find_element(By.XPATH, "//a[.='Register']").click()
        self.driver.find_element(By.ID, "input-firstname").send_keys("Bredlin")
        self.driver.find_element(By.ID, "input-lastname").send_keys("Jose")
