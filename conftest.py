import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from time import sleep

@pytest.fixture()
def set_up_browser():
    options = ChromeOptions()
    driver = webdriver.Chrome(options=options)
    options.page_load_strategy = 'none'
    driver.implicitly_wait(60)
    yield driver
    sleep(5)
    driver.quit()
