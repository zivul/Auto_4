from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import Keys
from time import sleep
import allure

@allure.feature('Тестирование web-приложений')
@allure.story('Объекты тестирования')
class TestExemple():
    @allure.title('Очистка поля поиска и ввод текста на github')
    def test_search(self, set_up_browser):
        driver = set_up_browser
        with allure.step('Открытие страницы'):
            driver.get('https://github.com/microsoft/vscode/issues')
        with allure.step('Клик в окно'):
            driver.find_element(By.XPATH, "(//*[contains(text(), 'Search or jump to...')])").click()
        with allure.step('Очищение окна'):
            driver.find_element(By.ID, 'query-builder-test').clear()
        with allure.step('Ввод текста и Enter'):
            driver.find_element(By.ID, 'query-builder-test').send_keys('bug' + Keys.ENTER)

    @allure.title('Ввод текста в поле и поиск на github')
    def test_filter(self, set_up_browser):
        driver = set_up_browser
        with allure.step('Открытие страницы'):
            driver.get('https://github.com/microsoft/vscode/issues')
        with allure.step('Клик в поле'):
            driver.find_element(By.XPATH, "(//span[@class='dropdown-caret hide-sm'])[1]").click()
        with allure.step('Ввод текста'):
            el = driver.find_element(By.ID, 'author-filter-field')
            text = 'bpasero'
            for i in text:
                el.send_keys(i)
                sleep(0.5)
        with allure.step('Клик на кнопку'):
            driver.find_element(By.CLASS_NAME, 'js-new-item-name').click()

    @allure.title('Заполнение формы на github')
    def test_language(self, set_up_browser):
        driver = set_up_browser
        with allure.step('Открытие страницы'):
            driver.get('https://github.com/search/advanced')
        with allure.step('Открытие поиска и клик'):
            driver.find_element(By.ID, 'search_language').click()
        with allure.step('Клик по кнопке'):
            driver.find_element(By.XPATH, "(//*[contains(text(), 'Python')])[1]").click()
        sleep(2)
        with allure.step('Ввод текста: <20000'):
            driver.find_element(By.ID, 'search_stars').send_keys('>20000')
        sleep(2)
        with allure.step('Ввод текста: environment.yml '):
            driver.find_element(By.ID, 'search_filename').send_keys('environment.yml')
        sleep(2)
        with allure.step('Клик по кнопке'):
            driver.find_element(By.XPATH, "(//button[@class='btn flex-auto'])[2]").click()

    @allure.title('Проверка фильтра на skillbox')
    def test_skillbox(self, set_up_browser):
        driver = set_up_browser
        with allure.step('Открытие формы'):
            driver.get('https://skillbox.ru/code/')
        with allure.step('Check-box выбор позиции: Профессия'):
            driver.find_element(By.XPATH, "(//*[contains(text(), 'Профессия')])[3]").click()
        with allure.step('Передвижение ползунков'):
            action_chains = webdriver.ActionChains(driver)
            left_button_slider = driver.find_element(By.XPATH, "//div[@aria-valuetext='1']")
            right_button_slider = driver.find_element(By.XPATH, "//div[@aria-valuetext='24']")
            action_chains.click_and_hold(left_button_slider).move_by_offset(16, 0).perform()
            action_chains.click_and_hold(right_button_slider).move_by_offset(-34, 0).pause(1).perform()
        with allure.step('Check-box выбор позиции: 1С'):
            driver.find_element(By.XPATH, "//span[@class='ui-checkbox-field__value ui-checkbox-field__value--small']")\
        .click()

    @allure.title('Наведение на график мышкой на github')
    def test_week(self, set_up_browser):
        driver = set_up_browser
        with allure.step('Открытие страницы github'):
            driver.get('https://github.com/microsoft/vscode/graphs/commit-activity')
        sleep(5)
        with allure.step('Наведение на элемент графика'):
            el = driver.find_element(By.XPATH, "(//*[@class='bar mini'])[22]")
            action = webdriver.ActionChains(driver)
            action.move_to_element(el).pause(1).perform()


