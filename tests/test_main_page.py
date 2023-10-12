import time

from tests.test_base import TestBase


class TestMain(TestBase):

    def test_go_to_tab_city(self):
        self.APP.actions_in_main_page.click_tab_city()
        assert self.APP.actions_in_main_page.get_city_name_on_tab_city() == 'Нижний Новгород'

    def test_assert_search_in_main_page(self):
        text = 'Гвозди'
        self.APP.actions_in_main_page.send_keys_in_search(text)
        self.APP.actions_in_main_page.click_button_search()
        time.sleep(5)
        assert 'mail.ru/search' in self.APP.actions_in_main_page.get_current_url()
        assert self.APP.search_page.check_element_search()
        assert self.APP.search_page.get_text_tab_search() == 'Поиск'

    def test_go_to_tab_games(self):
        self.APP.actions_in_main_page.click_button_games()
        assert self.APP.actions_in_main_page.get_name_on_tab_games() == 'Игры'


    def test_tab_auto(self):
        self.APP.actions_in_main_page.click_button_auto()
        assert self.APP.actions_in_main_page.get_name_on_tab_auto() == 'Авто'
