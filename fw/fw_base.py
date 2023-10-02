from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, ElementNotVisibleException, TimeoutException
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

class FWBase:

    def __init__(self, ApplicationManager):
        self.manager = ApplicationManager

    def click_element(self, locator):
        web_element = self.find_element(locator)
        web_element.click()

    def find_element(self, locator):
        web_element = WebDriverWait(self.GetDriver(), 30).until(EC.presence_of_element_located(locator))
        return web_element

    def GetDriver(self):
        if self.manager.driver_instance.driver is None:
            self.manager.driver_instance.get_driver()
        return self.manager.driver_instance.driver

    def send_keys_in_i_frame(self, locator_frame, locator_input, text):
        frame = self.find_element(locator_frame)
        self.GetDriver().switch_to.frame(frame)
        self.send_keys(locator_input, text)
        self.GetDriver().switch_to.default_content()

    def switch_to_i_frame(self, locator):
        frame = self.find_element(locator)
        self.GetDriver().switch_to.frame(frame)

    def switch_to_default(self):
        self.GetDriver().switch_to.default_content()

    def send_keys(self, locator, text):
        web_element = self.find_element(locator)
        web_element.send_keys(text)

    def get_current_url(self):
        return self.GetDriver().current_url

    def check_element_on_page(self, locator):
        try:
            self.find_element(locator)
            return True
        except:
            return False

    def get_attribute_text(self, locator):
        return self.find_element(locator).text
