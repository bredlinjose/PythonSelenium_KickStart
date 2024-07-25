import time
import os

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")

# cookies = driver.get_cookies()
# print("Length of the cookies:", len(cookies))
#
# for co in cookies:
#     print(co)
#     print("name:", co.get("name"), "value:", co.get("value"))

driver.add_cookie({"name": "my cookies", "value": "12345"})

cookies = driver.get_cookies()
print("Length of the cookies:", len(cookies))

# for co in cookies:
#     print(co)
#     print("name:", co.get("name"), "value:", co.get("value"))

driver.delete_cookie("my cookies")
cookies = driver.get_cookies()
for co in cookies:
    print(co)
    print("name:", co.get("name"), "value:", co.get("value"))

driver.delete_all_cookies()
print("Length of the cookies:", len(driver.get_cookies()))
