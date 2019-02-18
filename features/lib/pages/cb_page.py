from selenium.webdriver.common.by import By
from features.lib.pages.base_page_object import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time


class CbPage(BasePage):

    locator = {
        'Интернет-приемная': (By.XPATH, '//div[@class="header__extra-inner"]/div/span/a[@href="/Reception/"  '
                                        'and contains(text(), "Интернет-приемная")]'),
        'Написать благодарность': (By.XPATH, '//*[@href="/Reception/Message/Register?messageType=Gratitude"]'),
        'Ваша благодарность': (By.XPATH, '//*[@name="MessageBody"]'),
        'Я согласен': (By.XPATH, '//*[@type="checkbox" and contains(@data-title, "Согласие")]'),
        'Три полоски': (By.XPATH, '//div[@class="header__main"]/span/span[@class="burger"]'),
        'О сайте': (By.XPATH, '//li[@class="for_branch_11377"]/a[@href="/About/"]'),
        'Предупреждение': (By.XPATH, '//li[@data-catalogid="11380"]/div/a[contains(text(), "Предупреждение")]'),
        'Текст предупреждения': (By.XPATH, '//*[@id="content"]/p'),
        'en': (By.XPATH, '//li/a[@href="/Localization/SwitchLanguage?url=%2FAbout%2Fwarning%2F&from=ru-RU&to=en-GB"]')
    }

    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    def open_url(self, url):
        element = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(self.locator[url])
        )
        element.click()

    def write_message(self, field, text):
        element = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(self.locator[field])
        )
        element.send_keys(text)

    def check(self, chekcbox_text):
        element = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(self.locator[chekcbox_text])
        ).click()

    def menu(self, button):
        element = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(self.locator[button])
        ).click()

    def open_section(self, section):
        element = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(self.locator[section])
        ).click()

    def alarm_text(self):
        element = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(self.locator['Текст предупреждения'])
        )
        return element.text

    def change_language(self, language):
        element = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(self.locator[language])
        ).click()