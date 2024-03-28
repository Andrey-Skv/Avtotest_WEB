import pytest
import yaml
from module import Site

with open('datatest.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

# Фикстуры для входа

@pytest.fixture()
def set_locator1():
    return '''//*[@id="login"]/div[1]/label/input'''


@pytest.fixture()
def set_locator2():
    return '''//*[@id="login"]/div[2]/label/input'''


@pytest.fixture()
def set_locator3():
    return '''button'''


@pytest.fixture()
def set_locator4():
    return '''h2'''


@pytest.fixture()
def status_error():
    return '401'

# Фикстуры для верификации входа

@pytest.fixture()
def successful_login():
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""

@pytest.fixture()
def login():
    return "Hello, Ulrich"


@pytest.fixture(scope='session')
def site():
    site_instance = Site(data['address'])
    yield site_instance
    site_instance.quit()

# Фикстуры для элементов формы добавления поста

@pytest.fixture
def post_title_selector():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""

@pytest.fixture
def post_description_selector():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""

@pytest.fixture
def post_content_selector():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""

@pytest.fixture
def add_post_selector():
    return """//*[@id="create-item"]/div/div/div[7]/div/button/span"""

@pytest.fixture
def create_new_post():
    return """//*[@id="create-btn"]"""

@pytest.fixture
def check_title():
    return """//*[@id="app"]/main/div/div[1]/h1"""
    