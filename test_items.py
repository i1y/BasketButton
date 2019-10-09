import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_basket_button(browser):
    browser.get(link)
    time.sleep(10)
    try:
        browser.find_element(By.XPATH, '//button[@class = "btn btn-lg btn-primary btn-add-to-basket"]')
    except NoSuchElementException:
        assert False, "No basket button"

