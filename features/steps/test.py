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
    page = google_page.GooglePage(context)
    page.find_info(button_name)

@then('Нашли ссылку "{site}"')
def step_impl(context, site):
    page = google_page.GooglePage(context)
    page.find_url(site)


@then("Проверяем, что зашли на нужный сайт")
def step_impl(context):
    print(context.browser.current_url)



#@when('Открываем раздел {section}')
#def step_impl(context, section):
#    """
#    :type context: behave.runner.Context
#    """
#    raise NotImplementedError(u'STEP: When Открываем раздел "Написать благодарность"')
#
#
#@step('В поле {field} вводим значение {text}')
#def step_impl(context, field, text):
#    """
#    :type context: behave.runner.Context
#    """
#    raise NotImplementedError(u'STEP: And В поле "Ваша благодарность" вводим значение "случайный текст"')
#
#
#@step('Ставим галочку {verification}')
#def step_impl(context, verification):
#    """
#    :type context: behave.runner.Context
#    """
#    raise NotImplementedError(u'STEP: And Ставим галочку "Я согласен"')
#
#
#@then("Делаем скриншот")
#def step_impl(context):
#    screen = ImageGrab.grab()
#    screen.save(f"{os.path.abspath('Screenshots')}\\{datetime.time()}.jpg")
#
#
#
#@step('Нажимаем на раздел {section}')
#def step_impl(context, section):
#    """
#    :type context: behave.runner.Context
#    """
#    raise NotImplementedError(u'STEP: And Нажимаем на раздел "О сайте"')
#
#
#@when("Запоминаем текст предупреждения")
#def step_impl(context):
#    """
#    :type context: behave.runner.Context
#    """
#    raise NotImplementedError(u'STEP: When Запоминаем текст предупреждения')
#
#
#@step('Меняем язык страницы на {language}')
#def step_impl(context, language):
#    """
#    :type context: behave.runner.Context
#    """
#    raise NotImplementedError(u'STEP: And Меняем язык страницы на "en"')
#
#
#@when('Нажимаем на кнопку {button_name}')
#def step_impl(context, button_name):
#    """
#    :type context: behave.runner.Context
#    """
#    raise NotImplementedError(u'STEP: When Нажимаем на кнопку "Три полоски"')
#
#
#@step('Нажимаем на ссылку {url_text}')
#def step_impl(context, url_text):
#    """
#    :type context: behave.runner.Context
#    """
#    raise NotImplementedError(u'STEP: And Нажимаем на ссылку "Предупреждение"')