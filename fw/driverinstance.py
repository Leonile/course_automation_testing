from selenium import webdriver


class DriverInstance:

    driver = None

    def get_driver(self):
        options = webdriver.ChromeOptions()
        options.headless = False
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.set_script_timeout(600)
        self.driver.set_page_load_timeout(600)

        return self.driver

    def stop_driver(self):
        try:
            self.driver.quit()
            self.driver = None
        except:
            self.driver = None
