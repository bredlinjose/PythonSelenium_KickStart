import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

@pytest.fixture(params=["chrome", "edge", "firefox"])
def setup_and_teardown(request):
    global driver
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "edge":
        driver = webdriver.Edge()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://tutorialsninja.com/demo/")
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture()
def screenshot_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test", attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

