import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from time import sleep
import logging
import requests

logging.basicConfig(level=logging.DEBUG, filename='my_log.log',
                    format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]',
                    datefmt='%d/%m/%Y %I:%M:%S', encoding='utf-8', filemode='w')

logger = logging.getLogger(__name__)
handler = logging.FileHandler('test.log', encoding='utf-8')
formatter = logging.Formatter('%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info('Тестируем файл на данные')


@pytest.fixture()
def set_up_browser(page):
    options = ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(120)
    driver.maximize_window()
    yield driver
    driver.quit()



