from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def test_wait_page(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/')
        driver.find_element(By.XPATH, '//*[contains(text(), "Let’s build from here")]')

    def test_type(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/')
        WebDriverWait(driver, timeout=3).until(
            lambda d: d.find_element(By.XPATH, '//*[contains(text(), "Let’s build from here")]')
        )

    def test_form(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://m1vcki.csb.app/')
        # WebDriverWait(driver, timeout=30).until(lambda d: driver.find_element(By.ID, 'name')) #Ожидание загрузки этого поля
        driver.find_element(By.ID, 'name').send_keys('skillbox')
        driver.find_element(By.ID, 'email').send_keys('skillbox@mail.ru')
        driver.find_element(By.NAME, 'password').send_keys('skillbox')
        driver.execute_script('document.activeElement.blur()') #Отменяет действие поля
        driver.find_element(By.CSS_SELECTOR, '[role="checkbox"]').click()
        driver.find_element(By.XPATH, '//button/span[contains(text(), "Submit")]').click()
        WebDriverWait(driver, timeout=30).until(
            lambda d: d.find_element(By.XPATH, "//button/span[contains(text(), 'OK')]")   #Ожидание загрузки всплыв. окна
        )
        driver.find_element(By.XPATH, "//button/span[contains(text(), 'OK')]").click()

class TestValidate:
    def test_validate(self, set_up_browser):
        driver = set_up_browser
        a = 'skillbox'
        driver.get('https://m1vcki.csb.app/')
        el = driver.find_element(By.ID, 'name')
        el.send_keys(a)

        assert el.get_attribute('value') == 'skillbox_111'

    def test_checkbox(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://mkunc5.csb.app/')
        el = driver.find_element(By.CSS_SELECTOR, 'input')
        el.click()
        assert el.is_selected() is True
        pass
