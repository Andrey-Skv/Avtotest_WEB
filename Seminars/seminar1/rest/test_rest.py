""" Задание 2
Написать тест с использованием pytest и requests, в котором:
● Адрес сайта, имя пользователя и пароль хранятся в config.yaml
● conftest.py содержит фикстуру авторизации по адресу
  с передачей параметров
“username" и "password" и возвращающей токен авторизации
● Тест с использованием DDT проверяет наличие поста
с определенным заголовком в списке постов другого
пользователя, для этого выполняется get запрос по адресу
https://test-stand.gb.ru/api/posts c хедером, содержащим токен
авторизации в параметре "X-Auth-Token". Для отображения
постов другого пользователя передается "owner": "notMe". 

Задание 3
Условие: Добавить в задание с REST API ещё один тест, в котором создаётся новый пост,
 а потом проверяется его наличие на сервере по полю «описание».
Подсказка: создание поста выполняется запросом к https://test-stand.gb.ru/api/posts с 
передачей параметров title, description, content.
"""

import requests
import yaml
import pytest

with open("config.yaml", 'r') as stream:
    config_data = yaml.safe_load(stream)
site_url = config_data['site_url']

def test_check_not_my_post(auth_token):
    get_posts_url = f"{site_url}/api/posts"
    headers = {'X-Auth-Token': auth_token}
    owner = 'notMe'
    payload = {"owner": owner}
    response = requests.get(get_posts_url, headers=headers, params=payload)
    posts = response.json()['data']
    expected_post_title = config_data['title']
    post_titles = [post['title'] for post in posts]
    assert expected_post_title in post_titles

def test_create_post(auth_token):
    create_post_url = f"{site_url}/api/posts"
    headers = {'X-Auth-Token': auth_token}
    post_data = {
        "title": "New Post Title",
        "description": "New Post Description",
        "content": "New Post Content"
    }
    response = requests.post(create_post_url, headers=headers, json=post_data)
    assert response.status_code == 200  # Проверяем, что пост был создан успешно
def test_check_created_post(auth_token):
    # Теперь проверим наличие созданного поста по полю "описание"
    get_posts_url = f"{site_url}/api/posts"
    headers = {'X-Auth-Token': auth_token}
    response = requests.get(get_posts_url, headers=headers)
    posts = response.json()['data']
    new_post_description = "New Post Description"
    post_descriptions = [post['description'] for post in posts]
    assert new_post_description in post_descriptions