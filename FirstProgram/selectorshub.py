import os
import time

from selenium import webdriver
from selenium.common import ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

downloadPath = "C:\\Users\\Lenovo\\PycharmProjects\\PythonSelenium_KickStart\\files"
uploadPath = "C:\\Users\\Lenovo\\PycharmProjects\\PythonSelenium_KickStart\\files\\dummy.png"
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {"download.default_directory": downloadPath})
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://selectorshub.com/')
wait = WebDriverWait(driver, 15)
wait.until(expected_conditions.url_contains('https://selectorshub.com/'))

practicePageLnk = driver.find_element(By.XPATH, "//a[text()='PracticePage']")
practicePageLnk.click()

wait.until(expected_conditions.url_contains('xpath-practice-page'))
pageTitle = driver.title

emailTb = driver.find_element(By.XPATH, "//input[@title='Email']")
emailTb.send_keys('bredlinjose@yahoo.com')
passwordTb = driver.find_element(By.CSS_SELECTOR, 'input[title=Password]')
passwordTb.send_keys('bred123')
companyTb = driver.find_element(By.XPATH, "//div[@class='element-companyId']/descendant::input[@name='company']")
companyTb.send_keys('UTH UK')
mobileNumberTb = driver.find_element(By.XPATH,
                                     "//div[@class='element-companyId']/descendant::input[@name='mobile number']")
mobileNumberTb.send_keys('8526003286')
submitBtn = driver.find_element(By.XPATH, "//button[text()='Submit']")

firstCrushTb = driver.find_element(By.XPATH, "//input[@ placeholder='First Crush']")
firstCrushTb.send_keys('No Crush')

inspectElementTxt = driver.find_element(By.XPATH, "//div[@data-widget_type='html.default']/div/span[text()]")
print(inspectElementTxt.text)

enterNameHereTxt = driver.find_element(By.XPATH, "//*[name()='svg' and @onclick='nameField()']")
firstNameTb = driver.find_element(By.XPATH, "//input[@class='nameFld' and @placeholder='First Enter name']")

act = ActionChains(driver)

if not firstNameTb.is_enabled():
    # act.move_to_element(enterNameHereTxt).perform()
    act.scroll_by_amount(100, -250).perform()
    enterNameHereTxt.click()
    wait.until(expected_conditions.element_to_be_clickable(firstNameTb))
    firstNameTb.send_keys('Bredlin')
else:
    firstNameTb.send_keys('Bredlin')

lastNameTb = driver.find_element(By.XPATH, "//input[@class='nameFld' and @placeholder='Enter Last name']")
try:
    if not lastNameTb.is_enabled():
        enterNameHereTxt.click()
        lastNameTb.send_keys('Jose')
    else:
        lastNameTb.send_keys('Jose')
except ElementNotInteractableException:
    print('Last Name textbox is disabled')

pickDateTb = driver.find_element(By.ID, 'datepicker')
attributeValue = pickDateTb.get_attribute('value')
print('Value:', attributeValue)

dateTb = driver.find_element(By.NAME, 'the_date')
dateTb.send_keys('22-02-1997')

chooseCarDd = driver.find_element(By.ID, 'cars')
select = Select(chooseCarDd)
select.select_by_visible_text('Audi')
select.select_by_index(2)

checkoutHereBtn = driver.find_element(By.XPATH, "//button[text()='Checkout here']")
checkoutHereBtn.click()

parentHandle = driver.current_window_handle

tryTestcaseStudioLnk = driver.find_element(By.XPATH, "//div[@class='dropdown-content']/a[text()='Try TestCase Studio']")
wait.until(expected_conditions.visibility_of(tryTestcaseStudioLnk)).click()

driver.switch_to.window(driver.window_handles[1])
wait.until(expected_conditions.title_contains('SelectorsHub'))
url = driver.current_url
print('URL:', url)
driver.close()

driver.switch_to.window(parentHandle)

emailTb.clear()
emailTb.send_keys('bredlinjose@gmail.com')

# canvas
canvas = driver.find_element(By.XPATH, "//canvas[@id='canpro']")

usernameCb = driver.find_element(By.XPATH, "//a[.='Jordan.Mathews']/../../td/input")
usernameCb.click()

usernameCb1 = driver.find_element(By.XPATH, "//a[.='Joe.Root']/../../td/input")
usernameCb1.click()

userRoleTxt = driver.find_element(By.XPATH, "//a[.='John.Smith']/../following-sibling::td")
role = userRoleTxt.text
print('Role:', role)

# cross origin iframe
driver.get("https://selectorshub.com/cross-origin-iframe/")
iframe = driver.find_element(By.XPATH, "//p/iframe[@loading='lazy' and contains(@src,'docs.google.com')]")
driver.switch_to.frame(iframe)

yesCb = driver.find_element(By.XPATH, "//span[@dir='auto' and .='Yes']")
yesCb.click()

driver.switch_to.parent_frame()

shopFrame = driver.find_element(By.XPATH, "//iframe[@id='shop_frame']")
driver.switch_to.frame(shopFrame)
# time.sleep(5)  # scroll manually
act.scroll_by_amount(100, 400).perform()

# we can use only CSS_SELECTOR to interact with the element inside the shadow root
shadow_host1 = driver.find_element(By.CSS_SELECTOR, "shop-app[page='home']").shadow_root
shadow_host1.find_element(By.CSS_SELECTOR, "a[href='/list/ladies_outerwear']").click()

shadow_host2 = shadow_host1.find_element(By.CSS_SELECTOR, "paper-icon-button[icon='shopping-cart']").shadow_root
shadow_host2.find_element(By.CSS_SELECTOR, "#icon").click()

driver.get("https://selectorshub.com/xpath-practice-page/")

frameScenariosLnk = driver.find_element(By.XPATH,
                                        "//h3/a[text()='Click here to practice iframe and nested iframe scenarios.']")
act.move_to_element(frameScenariosLnk).perform()
frameScenariosLnk.click()

driver.switch_to.window(driver.window_handles[1])
time.sleep(5)

# nested iframe
iframe1 = driver.find_element(By.XPATH, "//iframe[@id='pact1']")
driver.switch_to.frame(iframe1)
firstCrushTb = driver.find_element(By.XPATH, "//input[@id='inp_val']")
firstCrushTb.send_keys("User Unknown")
lostBtn = driver.find_element(By.ID, "lost")
lostBtn.click()

iframe2 = driver.find_element(By.XPATH, "//iframe[@id='pact2']")
driver.switch_to.frame(iframe2)
currentCrushTb = driver.find_element(By.ID, "jex")
currentCrushTb.send_keys("No Crush")
connectNowBtn = driver.find_element(By.ID, "connect")
connectNowBtn.click()

iframe3 = driver.find_element(By.XPATH, "//iframe[@id='pact3']")
driver.switch_to.frame(iframe3)
destinyTb = driver.find_element(By.ID, "glaf")
destinyTb.send_keys("Unknown Place")
closeBtn = driver.find_element(By.CSS_SELECTOR, "#close")
closeBtn.click()

driver.switch_to.parent_frame()
driver.close()
driver.switch_to.window(parentHandle)

# iframe inside the shadow dom
# shadowRoot = driver.find_element(By.CSS_SELECTOR, "#userName").shadow_root
# shadowDomLnk = shadowRoot.find_element(By.CSS_SELECTOR, "a[href='https://selectorshub.com/iframe-in-shadow-dom/']")
# shadowDomLnk.click()

driver.get("https://selectorshub.com/iframe-in-shadow-dom/")
act.scroll_by_amount(100, 100).perform()
shadow1 = driver.find_element(By.CSS_SELECTOR, "#userName").shadow_root
insideFrame = shadow1.find_element(By.CSS_SELECTOR, "#pact1")
driver.switch_to.frame(insideFrame)
destinyTb1 = driver.find_element(By.CSS_SELECTOR, "#glaf")
destinyTb1.send_keys("Heaven")

driver.back()

downloadLnk = driver.find_element(By.PARTIAL_LINK_TEXT, "Click to Download PNG File")
act.scroll_by_amount(300, -200).perform()
downloadLnk.click()

chooseFileBtn = driver.find_element(By.ID, "myFile")
chooseFileBtn.send_keys(uploadPath)

time.sleep(3)

openWindowAlertBtn = driver.find_element(By.XPATH, "//button[text()='Click To Open Window Alert']")
openWindowAlertBtn.click()

alert = driver.switch_to.alert
print(alert.text)
alert.accept()

openWindowPromptAlertBtn = driver.find_element(By.XPATH, "//button[text()='Click To Open Window Prompt Alert']")
openWindowPromptAlertBtn.click()
alert = driver.switch_to.alert
print(alert.text)
alert.send_keys("Hiii")
alert.accept()

openModalBtn = driver.find_element(By.ID, "myBtn")
openModalBtn.click()

modelHeaderTxt = driver.find_element(By.XPATH, "//div[@class='modal-header']/h2/a")
wait.until(expected_conditions.visibility_of(modelHeaderTxt))
print(modelHeaderTxt.text)
closeBtn = driver.find_element(By.XPATH, "//span[@class='close']")
closeBtn.click()
wait.until(expected_conditions.invisibility_of_element(closeBtn))
