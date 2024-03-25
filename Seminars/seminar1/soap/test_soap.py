import pytest
from soap import check_text

def test1(good_word, bad_word):
    assert good_word in check_text(bad_word)
    # assert True