from fw.fw_base import FWBase
from selenium.webdriver.common.by import By


class Locator:
    tab_city = (By.XPATH, '//a[@data-testid="news-tabs-tab-item-regional"]')
    city_name = (By.XPATH, '//a[contains(@class, "is-active")]')
    input_search = (By.XPATH, '//input[@class="arrow__input mini-suggest__input"]')
    iframe_search = (By.XPATH, '//iframe[contains(@class, "search-arrow__frame")]')
    button_search = (By.XPATH, '//button[@data-testid="search-button"]')


class ActionsInMainPage(FWBase):

    def click_tab_city(self):
        self.click_element(Locator.tab_city)
        return self

    def get_city_name_on_tab_city(self):
        return self.find_element(Locator.city_name).text

    def send_keys_in_search(self, text):
        self.send_keys_in_i_frame(Locator.iframe_search, Locator.input_search, text)
        return self

    def click_button_search(self):
        self.click_element(Locator.button_search)
        return self
