""" Задание 1. Оптимизация примера из лекции
Доработать пример из лекции следующим образом:
вынести все локаторы элементов в фикстуры в conftest.py
вынести ожидаемый результат в фикстуру в conftest.py
добавить завершение работы Selenium после теста
вынести время ожидания в конфигурационный файл testdata.yaml

Задание 2
Доработать программу, полученную в предыдущем задании
добавив туда шаг, в котором будет проверяться успешность
входа пользователя при вводе верного имени и пароля.
Имя и пароль должны храниться в конфигурационном файле.  

Задание 3
Условие: Добавить в наш тестовый проект шаг добавления поста после входа. Должна выполняться
проверка на наличие названия поста на странице сразу после его создания.
Совет: не забудьте добавить небольшие ожидания перед и после нажатия кнопки создания поста."""

import yaml
from module import Site
import time


with open('datatest.yaml') as f:
    data = yaml.safe_load(f)

# site = Site(data['address'])

def test_1(site, set_locator1, set_locator2, set_locator3, set_locator4, status_error):
    selector1 = set_locator1
    input1 = site.find_element('xpath', selector1)
    input1.send_keys('take')
    selector2 = set_locator2
    input2 = site.find_element('xpath', selector2)
    input2.send_keys('gta')
    selector3 = set_locator3
    input3 = site.find_element('css', selector3)
    input3.click()
    selector4 = set_locator4
    find1 = site.find_element('css', selector4)
    assert find1.text == status_error
    time.sleep(data['sleep_time'])
    selector1 = set_locator1
    input1 = site.find_element('xpath', selector1)
    input1.clear()
    selector2 = set_locator2
    input2 = site.find_element('xpath', selector2)
    input2.clear()


def test_2(site, set_locator1, set_locator2, set_locator3, successful_login, login):
    selector1 = set_locator1
    input1 = site.find_element('xpath', selector1)
    input1.send_keys(data['username'])
    selector2 = set_locator2
    input2 = site.find_element('xpath', selector2)
    input2.send_keys(data['password'])
    selector3 = set_locator3
    input3 = site.find_element('css', selector3)
    input3.click()
    selector4 = successful_login
    find1 = site.find_element('xpath', selector4)
    assert find1.text == login
    time.sleep(data['sleep_time'])

def test_3(site, create_new_post, post_title_selector, post_description_selector, post_content_selector,
add_post_selector, check_title):
    selector1 = create_new_post
    input1 = site.find_element('xpath', selector1)
    input1.click()
    time.sleep(data['sleep_time'])
    selector2 = post_title_selector
    input2 = site.find_element('xpath', selector2)
    input2.send_keys('New Post Title')
    selector3 = post_description_selector
    input3 = site.find_element('xpath', selector3)
    input3.send_keys('New Post Description')
    selector4 = post_content_selector
    input4 = site.find_element('xpath', selector4)
    input4.send_keys('New Post Content')
    selector5 = add_post_selector
    input5 = site.find_element('xpath', selector5)
    input5.click()
    selector6 = check_title
    find1 = site.find_element('xpath', selector6)
    assert find1.text == 'Create Post'
    time.sleep(data['sleep_time'])