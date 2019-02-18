from selenium.webdriver.common.by import By
from features.lib.pages.base_page_object import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time


class CbPage(BasePage):

    locator={}

    def __init__(self, context):
        BasePage.__init__(self, context.browser)