from selenium import webdriver # selenium
from selenium.webdriver.common.by import By  #Для перехода к элементу
from time import sleep  #Задержка показа сайта


# driver = webdriver.Chrome()
# driver.get('https://apteka-altay.ru/')
# driver.find_element(By.LINK_TEXT, 'Косметика ').click()
# driver.quit()

browser = webdriver.Chrome()  #Открываем браузер (Chrome)
browser.get('https://apteka-altay.ru/sobachij-zhir') #Переход на сайт
click_b = browser.find_element(By.ID, 'button-cart') #Находим элемент по ID
click_b.click()

