import pytest
import requests
import yaml

@pytest.fixture(scope="session")
def auth_token():
    with open("config.yaml", 'r') as stream:
        config_data = yaml.safe_load(stream)
    login_url = f"{config_data['site_url']}/gateway/login"
    username = config_data['username']
    password = config_data['password']
    response = requests.post(login_url, data={"username": username, "password": password})
    return response.json()['token']