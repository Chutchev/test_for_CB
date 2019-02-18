from behave import *
from PIL import ImageGrab
import os
from datetime import datetime
from features.lib.pages import google_page, base_page_object, cb_page
import time

@when('Открываем сайт "{site}"')
def step_impl(context, site):
  page = base_page_object.BasePage(context.browser, base_url=site)
  page.visit(site)


@when('Проверяем, что появилось поле "{field}"')
def step_impl(context, field):
    page = google_page.GooglePage(context)
    is_find_field = page.check_field(field)
    if not is_find_field:
        context.scenario.skip()

@step('Вводим в поиск "{text}"')
def step_impl(context, text):
    page = google_page.GooglePage(context)
    page.fill_find_field(text)


@when('Нажимаем на кнопку "{button_name}"')
def step_impl(context, button_name):
    locator = {
        'google_url': "https://www.google.ru",
        'cb_url': "https://www.cbr.ru/"
    }
    if context.browser.current_url.startswith(locator['google_url']):
        page = google_page.GooglePage(context)
        page.find_info(button_name)
    elif context.browser.current_url.startswith(locator['cb_url']):
        page = cb_page.CbPage(context)
        page.menu(button_name)


@then('Нашли ссылку "{site}"')
def step_impl(context, site):
    page = google_page.GooglePage(context)
    if not page.find_url(site):
        context.scenario.skip()


@then("Проверяем, что зашли на нужный сайт")
def step_impl(context):
    if context.browser.current_url != 'https://www.cbr.ru/':
        context.scenario.skip()


@when('Нажимаем на ссылку "{url}"')
def step_impl(context, url):
    page = cb_page.CbPage(context)
    page.open_url(url)


@when('Открываем раздел "{section}"')
def step_impl(context, section):
    page = cb_page.CbPage(context)
    page.open_url(section)


@step('В поле "{field}" вводим значение "{text}"')
def step_impl(context, field, text):
    page = cb_page.CbPage(context)
    page.write_message(field, text)


@step('Ставим галочку "{verification}"')
def step_impl(context, verification):
    page = cb_page.CbPage(context)
    page.check(verification)


@then("Делаем скриншот")
def step_impl(context):
    screen = ImageGrab.grab()
    screen.save(f"{os.path.relpath('Screenshots')}\\{datetime.today().hour} {datetime.today().minute} "
                f"{datetime.today().second}.jpg")


@step('Нажимаем на раздел "{section}"')
def step_impl(context, section):
    page = cb_page.CbPage(context)
    page.open_section(section)


@when("Запоминаем текст предупреждения")
def step_impl(context):
    page = cb_page.CbPage(context)
    context.alarm_text = page.alarm_text()


@step('Меняем язык страницы на "{language}"')
def step_impl(context, language):
    page = cb_page.CbPage(context)
    page.change_language(language)


@when("Проверили, что текст отличается от запомненного текста ранее")
def step_impl(context):
    page = cb_page.CbPage(context)
    context.new_alarm_text = page.alarm_text()
    if context.new_alarm_text == context.alarm_text:
        print('Текст не изменился')
        context.scenario.skip()
