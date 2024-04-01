""" Доработать проект так, чтобы он использовал Page Object

Условие: Добавить в проект тест по проверке механики работы формы Contact Us на главной странице личного кабинета.
Должно проверятся открытие формы, ввод данных в поля, клик по кнопке и появление всплывающего alert.

Совет: переключиться на alert можно командой alert = self.driver.switch_to.alert
Вывести текст alert.text
 """

import time
import yaml
from testpage import OperationsHelper
import logging


with open('datatest.yaml') as f:
    data = yaml.safe_load(f)
status_error = data['status_error']
adress = data['address']

def test_1(browser):
    logging.info("Test 1 Starting")
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login('test')
    test_page.enter_pass('test')
    test_page.click_login_button()
    assert test_page.get_error_text() == status_error
    time.sleep(data['sleep_time'])

def test_2(browser):
    logging.info("Test 2 Starting")
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login(data['username'])
    test_page.enter_pass(data['password'])
    test_page.click_login_button()
    assert test_page.check_login_success() == "Hello, Ulrich"
    time.sleep(data['sleep_time'])


def test_3(browser):
    logging.info("Test 3 Starting")
    test_page = OperationsHelper(browser)
    test_page.create_post(data['title'], data['description'], data['content'])
    
def test_4(browser):
    logging.info("Test 4 Starting")
    test_page = OperationsHelper(browser)
    test_page.test_contact_us()