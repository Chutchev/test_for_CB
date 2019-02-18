from selenium.webdriver import *


class BasePage(object):

    def __init__(self, browser, base_url="https://www.google.ru/"):
        self.browser = browser
        self.base_url = base_url

    def find_element(self, *loc):
        return self.browser.find_element(*loc)

    def visit(self, url):
        self.browser.get(url)
