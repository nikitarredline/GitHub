import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_items(browser):
    browser.get(link)
    time.sleep(5)
    browser.find_element_by_xpath("//button[@class='btn btn-lg btn-primary btn-add-to-basket']")