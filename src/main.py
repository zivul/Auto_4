from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver

def test_open_website_and_check_title():
    options = ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get("https://skillbox.ru")
    assert 'Skillbox – образовательная платформа с онлайн-курсами.' == driver.title
    driver.quit()


