import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://test-stand.gb.ru"

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                            message=f"Can't find element by locator {locator}")
        except:
            logging.exception("Find element exception")
            element = None
        return element


    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(property)
        else:
            logging.exception(f'Property {property} not found element with locator {locator}')
            return None

    def go_to_site(self):
        try:
            start_browser = self.driver.get(self.base_url)
        except:
            logging.exception("Go to site exception")
            start_browser = None
        return start_browser

    def get_alert_text(self):
        try:
            alert = self.driver.switch_to.alert
            text = alert.text
            logging.info(f'We found text {text} in alert')
            return text
        except:
            logging.exception("Get alert text exception")
            return None