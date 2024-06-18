from selenium.webdriver.common.by import By

class TestWait:
    def test_wait_page(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/')
        driver.find_element(By.XPATH, '//*[contains(text(), "Let’s build from here")]')

    def test_type(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/')
        driver.find_element(By.XPATH, '//*[contains(text(), "Let’s build from here")]')