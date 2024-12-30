class Browser:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def close_browser(self):
        self.driver.quit()

    def get_current_url(self):
        return self.driver.current_url