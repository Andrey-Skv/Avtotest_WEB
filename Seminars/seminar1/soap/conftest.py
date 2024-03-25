import pytest

@pytest.fixture
def good_word():
    return "Корова"

@pytest.fixture
def bad_word():
    return "Корва"