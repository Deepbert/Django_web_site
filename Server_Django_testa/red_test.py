import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

def test_title(browser):

    browser.get('http://127.0.0.1:8000/home/')

    assert browser.title == 'Server4'



