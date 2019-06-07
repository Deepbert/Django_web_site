import pytest
import time
from selenium import webdriver

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

def test_title(browser):

    browser.get('http://127.0.0.1:8000/home/')

    header_text = browser.find_element_by_tag_name('h1').text

    inputbox = browser.find_element_by_id('First_ID')

    inputbox.send_keys('HHHhhh')

    assert header_text == 'Server_hh'

    assert browser.title == 'Server4'




