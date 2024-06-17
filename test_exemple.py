
class TestExemple:
    def test_exemple_1(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://skillbox.ru')
        assert 'Skillbox – образовательная платформа с онлайн-курсами.' == driver.title

    def test_exemple_2(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://skillbox.ru')
        assert 'Skillbox – образовательная платформа с онлайн-курсами.' == driver.title

    def test_exemple_3(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://skillbox.ru')
        assert 'Skillbox – образовательная' == driver.title







