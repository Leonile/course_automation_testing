from fw.application_manager import ApplicationManager
from data.settings import Settings


class TestBase:

    APP = ApplicationManager()

    def setup_method(self):
        self.APP.driver_instance.get_driver().get(Settings.main_page)

    def teardown_class(self):
        self.APP.driver_instance.stop_driver()

    def teardown_method(self):
        print(123123123123)