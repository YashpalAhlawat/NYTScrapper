from scrapper.base import BaseScrapper
from scrapper.config.config_reader import ConfigReader
from scrapper.helper import *


class LatestNewsScrapper(BaseScrapper):
    def __init__(self):
        super().__init__()

    def execute(self):
        cf = ConfigReader()
        cf.load_config()
        get_website(self.driver, cf)
        login(self.driver, cf)
        # Added just to go back to screen as unable to pass captcha
        reset(self.driver, cf)
        select_tech(self.driver)
        post_titles, post_descriptions, post_authors = self.extract_latest_news_section(cf)
        response = self.generate_response(post_titles, post_descriptions, post_authors)
        return response

    def extract_latest_news_section(self, cf):
        soup = scrap_specific_section(self.driver.current_url, cf.get("post_section_id"))
        close_driver(self.driver)
        post_titles = soup.findAll("h2", {"class": "css-1j9dxys e15t083i0"})
        post_descriptions = soup.findAll('p', {"class": "css-1echdzn e15t083i1"})
        post_authors = soup.findAll(class_='css-1xonkmu')
        return post_titles, post_descriptions, post_authors

    @staticmethod
    def generate_response(post_titles, post_descriptions, post_authors):
        response = []
        for i in range(len(post_titles)):
            data = {"title": encode_decode_string(post_titles[i].text),
                    "description": encode_decode_string(post_descriptions[i].text),
                    "author": encode_decode_string(post_authors[i].text)}
            response.append(data)
        return response




