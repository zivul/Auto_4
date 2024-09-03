from selenium.webdriver.common.by import By
import allure
from conftest import *

users = ['j_username1', 'j_username2', 'j_username3']
passws = ['111', '222', '333']
def generates_pairs():
    pdd = []
    for user in users:
        for passw in passws:
            pdd.append(pytest.param((user, passw), id=f'{users}, {passws}'))
    return pdd


@allure.feature('Тестирование формы')
@allure.story('Объекты тестирования')
class TestCount:
    @pytest.mark.parametrize('creds', generates_pairs())
    @pytest.mark.skip
    def test_defoltcount(self, set_up_browser, creds):
        login, passw = creds
        driver = set_up_browser
        driver.get('https://lk.platformaofd.ru/web/login')
        driver.find_element(By.ID, 'j_username').send_keys(login)
        driver.find_element(By.ID, 'j_password').send_keys(passw)
        driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary btn-block']").click()
        el = driver.find_element(By.ID, "j_username.errors").text
        assert "Значение указано неверно" == el

    @pytest.mark.skip
    def test_xxx(self, set_up_browser):
        set_up_browser.get('https://yandex.ru/support/webmaster/recommendations/site-structure.html#site-structure')
        el = set_up_browser.find_element(By.ID, 'ariaid-title1').text
        assert 'Структура сайта' == el

    def test_yyy(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://lk.platformaofd.ru/web/login')
        driver.find_element(By.ID, 'j_username').send_keys('login')
        driver.find_element(By.ID, 'j_password').send_keys('passw')
        driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary btn-block']").click()
        el = driver.find_element(By.ID, "j_username.errors").text
        assert "Значение указано неверно" == el


# @pytest.fixture()
# def test_zzz(go_to, wait_element):
#     go_to('https://skillbox.ru/')
#     wait_element('(//a[contains(text(), "Психология")])[1]')










