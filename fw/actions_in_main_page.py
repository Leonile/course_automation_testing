from fw.fw_base import FWBase
from selenium.webdriver.common.by import By


class Locator:
    tab_city = (By.XPATH, '//a[@data-testid="news-tabs-tab-item-regional"]')
    city_name = (By.XPATH, '//a[contains(@class, "is-active")]')
    input_search = (By.XPATH, '//input[@class="arrow__input mini-suggest__input"]')
    iframe_search = (By.XPATH, '//iframe[contains(@class, "search-arrow__frame")]')
    button_search = (By.XPATH, '//button[@data-testid="search-button"]')
    button_games = (By.XPATH, '//a[@data-testid="news-tabs-tab-item-games"]')
    button_auto = (By.XPATH, '//a[@data-testid="news-tabs-tab-item-auto"]')

class ActionsInMainPage(FWBase):

    def click_tab_city(self):
        self.click_element(Locator.tab_city)
        return self

    def get_city_name_on_tab_city(self):
        return self.find_element(Locator.city_name).text

    def get_name_on_tab_games(self):
        return self.find_element(Locator.button_games).text

    def send_keys_in_search(self, text):
        self.send_keys_in_i_frame(Locator.iframe_search, Locator.input_search, text)
        return self

    def click_button_search(self):
        self.click_element(Locator.button_search)
        return self

    def click_button_games(self):
        self.click_element(Locator.button_games)
        return self

    def click_button_auto(self):
        self.click_element(Locator.button_auto)
        return

    def get_name_on_tab_auto(self):
        return self.find_element(Locator.button_auto).text