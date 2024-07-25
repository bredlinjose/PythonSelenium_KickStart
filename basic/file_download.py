import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

location = os.path.dirname(os.path.abspath('.')) + '\\files\\download'
print(location)
def browser_setup(browser):
    global driver
    if str.lower(browser) == 'chrome':
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option("prefs", {"download.default_directory": location})
        opt.add_experimental_option('detach', False)  # close browser
        driver = webdriver.Chrome(options=opt)
    elif str.lower(browser) == 'edge':
        opt = webdriver.EdgeOptions()
        opt.add_experimental_option("prefs", {"download.default_directory": location})
        opt.add_experimental_option('detach', False)  # close browser
        driver = webdriver.Chrome(options=opt)
    elif str.lower(browser) == 'firefox':
        opt = webdriver.FirefoxOptions()
        opt.set_preference("browse.helperApps.neverAsk.saveToDisk", "application/msword")  # mime
        opt.set_preference("browse.download.manager.showWhenStarting", False)
        opt.set_preference("browse.download.folderList", 2)  # 0-desktop, 1-download folder, 2-desired location
        opt.set_preference("browse.download.dir", location)
        driver = webdriver.Firefox(opt)
    else:
        print('Enter the valid browser name...')
    return driver


def browser_teardown():
    driver.quit()


driver = browser_setup("chrome")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://file-examples.com/index.php/sample-documents-download/")
driver.find_element(By.XPATH, "//td[text()='DOC, DOCX']/../descendant::a").click()
driver.find_element(By.XPATH, "//a[text()='Download sample DOC file']").click()

time.sleep(10)
browser_teardown()
