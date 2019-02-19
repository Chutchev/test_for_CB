from selenium.webdriver.common.by import By
from features.lib.pages.base_page_object import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time

class GooglePage(BasePage):

    locator = {
        'поиск': (By.XPATH, "//*[@class='gLFyf gsfi']"),
        'Поиск в Google': (By.XPATH, "//*[@class='VlcLAe']/center/input[@value='Поиск в Google']"),
        "cbr.ru": (By.XPATH, "//*[@class='iUh30' and contains(text(), 'cbr')]")
    }

    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    def fill_find_field(self, text):
        self.find_element(*self.locator['поиск']).send_keys(text)

    def check_field(self, what):
        if what in self.locator.keys():
            wait_element = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(self.locator[what])
            )
            return True
        else:
            return False

    def find_info(self, button_name):
        try:
            wait_element = WebDriverWait(self.browser, 20).until(
                EC.presence_of_element_located(self.locator[button_name])
            )
            element = self.find_element(*self.locator[button_name])
            element.click()
        except ElementNotVisibleException:
            time.sleep(5)
            wait_element = WebDriverWait(self.browser, 20).until(
                EC.presence_of_element_located(self.locator[button_name])
            )
            element = self.find_element(*self.locator[button_name])
            element.click()

    def find_url(self, url):
        try:
            wait_element = WebDriverWait(self.browser, 20).until(
                EC.presence_of_element_located(self.locator[url])
            )
            return True
        except ElementNotVisibleException:
            return False




