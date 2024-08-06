class WebUtils:
    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, element):
        element = self.driver.find_element(*element)
        element.click()

    def clear_textfield(self, element):
        element = self.driver.find_element(*element)
        element.clear()

    def set_value_to_textfield(self, element, value):
        element = self.driver.find_element(*element)
        self.click_on_element(element)
        self.clear_textfield()
        element.send_keys(value)


