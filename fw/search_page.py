from selenium.webdriver.common.by import By

from fw.fw_base import FWBase

class Locator:
    search_frame = (By.XPATH, '//iframe[@class="yandex-frame"]')
    tab_selected = (By.XPATH, '//a[contains(@class, "Tab_selected")]')


class SearchPage(FWBase):

     def check_element_search(self):
         self.switch_to_i_frame(Locator.search_frame)
         return self.check_element_on_page(Locator.tab_selected)

     def get_text_tab_search(self):
         return self.get_attribute_text(Locator.tab_selected)