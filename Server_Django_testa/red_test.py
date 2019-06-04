from selenium import webdriver

def testy_test():

    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:8000/home/')

    print(driver.title)

    assert driver.title == 'Server4'



