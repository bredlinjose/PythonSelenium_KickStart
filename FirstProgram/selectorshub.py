from selenium import webdriver
from selenium.common import ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

options = webdriver.ChromeOptions()
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

emailTb = driver.find_element(By.XPATH,"//input[@title='Email']")
emailTb.send_keys('bredlinjose@yahoo.com')
passwordTb = driver.find_element(By.CSS_SELECTOR, 'input[title=Password]')
passwordTb.send_keys('bred123')
companyTb = driver.find_element(By.XPATH, "//div[@class='element-companyId']/descendant::input[@name='company']")
companyTb.send_keys('UTH UK')
mobileNumberTb = driver.find_element(By.XPATH, "//div[@class='element-companyId']/descendant::input[@name='mobile number']")
mobileNumberTb.send_keys('8526003286')
submitBtn = driver.find_element(By.XPATH, "//button[text()='Submit']")

firstCrushTb = driver.find_element(By.XPATH, "//input[@placeholder='First Crush']")
firstCrushTb.send_keys('No Crush')

inspectElementTxt = driver.find_element(By.XPATH, "//div[@data-widget_type='html.default']/div/span[text()]")
print(inspectElementTxt.text)

enterNameHereTxt = driver.find_element(By.XPATH, "//*[name()='svg' and @onclick='nameField()']")
firstNameTb = driver.find_element(By.XPATH, "//input[@class='nameFld' and @placeholder='First Enter name']")

act = ActionChains(driver)

if not firstNameTb.is_enabled():
    act.move_to_element(enterNameHereTxt).perform()
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
    print('Last Name Element is not Interactable')

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

