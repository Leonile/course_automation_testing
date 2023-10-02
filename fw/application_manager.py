from fw.actions_in_main_page import ActionsInMainPage
from fw.driverinstance import DriverInstance
from fw.search_page import SearchPage


class ApplicationManager:

    def __init__(self):
        self.driver_instance = DriverInstance()
        self.actions_in_main_page = ActionsInMainPage(self)
        self.search_page = SearchPage(self)