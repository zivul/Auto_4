import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from time import sleep

@pytest.fixture()
def set_up_browser():
    options = ChromeOptions()
    options.page_load_strategy = 'none' #статус ожидания. none - без ожидания, normal - по умолчанию
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(30)  #ожидание в сек. 30 сек будет загружаться
    yield driver
    sleep(5)
    driver.quit()
