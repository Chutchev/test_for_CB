from selenium import webdriver
import os

def before_all(context):
    context.browser = webdriver.Chrome(os.path.abspath("chromedriver.exe"))
    context.browser.maximize_window()


def after_all(context):
    screens_directory = os.path.abspath("Screenshots")
    for image in os.listdir(screens_directory):
        os.remove(os.path.join(screens_directory, image))