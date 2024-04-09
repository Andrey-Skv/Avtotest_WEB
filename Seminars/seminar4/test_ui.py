""" Доработать проект так, как это было сделано в лекции:
добавить обработку ошибок
вынести локаторы в yaml-файл
 добавить debug-логи

Иметь почту на сайте mail.ru (если ее нет – создать).
В настройках безопасности почтового ящика задать 
пароль для внешних приложений.
Написать скрипт, который отправляет по email 
отчет о тестах, сформированный pytest.
"""

from testpage import OperationHelper
import pytest
import logging
import yaml
import time


with open("datatest.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)



def test_step1(browser):
    logging.info("Test 1 Starting")
    testpage = OperationHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == data.get("status_error")


def test_step2(browser):
    logging.info("Test 2 Starting")
    testpage = OperationHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(data.get("username"))
    testpage.enter_pass(data.get("password"))
    testpage.click_login_button()
    assert testpage.get_user_text() == f"Hello, {data.get('username')}"


def test_step3(browser):
    logging.info("Test3 Starting")
    testpage = OperationHelper(browser)
    testpage.click_new_post_btn()
    testpage.enter_title(data.get("title"))
    testpage.enter_description(data.get("description"))
    testpage.enter_content(data.get("content"))
    testpage.click_save_btn()
    time.sleep(3)
    assert testpage.get_res_text() == data.get("title"), "Test FAILED!"


def test_step4(browser, send_mail):
    # test contact us
    logging.info("Test Contact_us Starting")
    testpage = OperationHelper(browser)
    testpage.click_contact_link()
    testpage.enter_contact_name(data.get("username"))
    testpage.enter_contact_email(data.get("email"))
    testpage.enter_contact_content(data.get("content"))
    testpage.click_contact_send_btn()
    assert testpage.get_allert_message() == "Form successfully submitted", "Test FAILED!"
    de = send_mail

