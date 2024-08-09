import allure
import pytest

from page_object_model.pages.home_page import HomePage
from page_object_model.pages.search_page import SearchPage


@pytest.mark.usefixtures("setup_and_teardown", "screenshot_on_failure")
@allure.severity(allure.severity_level.NORMAL)
class TestSearch:
    def test_search_valid_product(self):
        home_page = HomePage(self.driver)

        # home_page.set_value_on_search_textfield("HP")
        # search_page = home_page.click_on_search_icon()

        search_page = home_page.search_product("HP")
        assert search_page.display_valid_product_status()

    def test_search_empty_product(self):
        home_page = HomePage(self.driver)

        # home_page.set_value_on_search_textfield("")
        # search_page = home_page.click_on_search_icon()

        search_page = home_page.search_product("")
        assert search_page.display_invalid_product_status()

    def test_search_invalid_product(self):
        home_page = HomePage(self.driver)

        # home_page.set_value_on_search_textfield("Dell")
        # search_page = home_page.click_on_search_icon()

        search_page = home_page.search_product("Dell")
        assert search_page.display_invalid_product_status()
