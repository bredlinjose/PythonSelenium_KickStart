import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_valid_product(self):
        self.driver.find_element(By.NAME, "search").send_keys("HP")
        self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn-default')]").click()
        assert self.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()

    def test_search_invalid_product(self):
        self.driver.find_element(By.NAME, "search").send_keys("mobile")
        self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn-default')]").click()
        expected_text = "There is no product that matches the search criteria."
        actual_text = self.driver.find_element(By.XPATH, "//div[@id='content']/h2/following-sibling::p").text
        assert actual_text.__eq__(expected_text)

    def test_search_without_product(self):
        self.driver.find_element(By.NAME, "search").send_keys("")
        self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn-default')]").click()
        expected_text = "There is no product that matches the search criteria."
        actual_text = self.driver.find_element(By.XPATH, "//div[@id='content']/h2/following-sibling::p").text
        assert actual_text.__eq__(expected_text)
