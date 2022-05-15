from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup,SoupStrainer


# TODO Move common methods e.g. login here so that can be reused
def get_website(driver, cf):
    driver.get(cf.get("website"))


def login(driver, cf):
    login_btn = driver.find_element(By.LINK_TEXT, cf.get("login"))
    login_btn.click()
    email_input = driver.find_element(By.ID, cf.get("email_input_box_id", "email"))
    email_input.send_keys(cf.get("username"))
    email_input.send_keys(Keys.RETURN)
    driver.implicitly_wait(5)
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(cf.get("password"))
    time.sleep(5)
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)


def reset(driver, cf):
    if driver.current_url != cf.get("website"):
        driver.get(cf.get("website"))


def close_driver(driver):
    driver.close()


def select_tech(driver):
    driver.find_element(By.LINK_TEXT, "Tech").click()


def scrap_latest_post(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


def scrap_specific_section(url, section_id):
    only_section = SoupStrainer(id=section_id)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser", parse_only=only_section)
    return soup


def encode_decode_string(str_input):
    if not str_input:
        return None
    str_encode = str_input.encode("ascii", "ignore")
    str_decode = str_encode.decode()
    return str_decode





