from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class BaseScrapper:
    def __init__(self):
        self.driver = webdriver.Chrome('Resource/Driver/chromedriver')

    def execute(self):
        self.driver.get("https://www.python.org")
        print(self.driver.title)
        search_bar = self.driver.find_element_by_name("q")
        search_bar.clear()
        search_bar.send_keys("getting started with python")
        search_bar.send_keys(Keys.RETURN)
        print(self.driver.current_url)
        self.driver.close()
