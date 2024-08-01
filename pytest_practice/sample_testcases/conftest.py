import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

# @pytest.fixture()
# def log_on_failure(request):
#     yield
#     item = request.node
#     if item.rep_call.failed:
#         allure.attach(driver.get_screenshot_as_png(), name="failed_test", attachment_type=AttachmentType.PNG)
#
#
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)
#     return rep

@pytest.fixture()
def setup_and_teardown(request):
    # global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://tutorialsninja.com/demo/")
    request.cls.driver = driver
    yield
    driver.quit()
