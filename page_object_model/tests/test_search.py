import pytest

from page_object_model.pages.home_page import HomePage


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_valid_product(self):
        home = HomePage(self.driver)
        home.set_value_on_search_textfield("imac")
        home.click_on_search_icon()


    # def test_search_empty_product(self):
    #     pass
    #
    # def test_search_invalid_product(self):
    #     pass
