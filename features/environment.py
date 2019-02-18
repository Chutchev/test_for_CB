from selenium import webdriver
import os

def before_all(context):
    context.browser = webdriver.Chrome(os.path.abspath("chromedriver.exe"))
    context.browser.maximize_window()
