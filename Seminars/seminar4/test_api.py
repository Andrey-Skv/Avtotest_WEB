import requests
import yaml
import pytest
import logging

with open("datatest.yaml", 'r') as stream:
    config_data = yaml.safe_load(stream)
site_url = config_data['address']

def test_check_not_my_post(auth_token):
    logging.info("Test check not me post started")
    get_posts_url = f"{site_url}/api/posts"
    headers = {'X-Auth-Token': auth_token}
    owner = 'notMe'
    payload = {"owner": owner}
    response = requests.get(get_posts_url, headers=headers, params=payload)
    posts = response.json()['data']
    logging.info(f"response is: {posts}")
    expected_post_title = config_data['title']
    post_titles = [post['title'] for post in posts]
    assert expected_post_title in post_titles
    

def test_create_post(auth_token):
    logging.info("Test create post started")
    create_post_url = f"{site_url}/api/posts"
    headers = {'X-Auth-Token': auth_token}
    post_data = {
        "title": "New Post Title",
        "description": "New Post Description",
        "content": "New Post Content"
    }
    response = requests.post(create_post_url, headers=headers, json=post_data)
    logging.info(f"Response is {str(response)}")
    assert response.status_code == 200  # Проверяем, что пост был создан успешно


def test_check_created_post(auth_token):
    # Теперь проверим наличие созданного поста по полю "описание"
    logging.info("Test check created post started")
    get_posts_url = f"{site_url}/api/posts"
    headers = {'X-Auth-Token': auth_token}
    response = requests.get(get_posts_url, headers=headers)
    posts = response.json()['data']
    logging.info(f"Response is {str(response)}")
    new_post_description = "New Post Description"
    post_descriptions = [post['description'] for post in posts]
    assert new_post_description in post_descriptions