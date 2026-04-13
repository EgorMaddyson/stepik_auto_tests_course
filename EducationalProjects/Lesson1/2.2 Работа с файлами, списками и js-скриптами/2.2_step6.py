from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

# функция расчёта значения переменной для дальнейшего ввода в поле
    def calc(x):
        return str(math.log(abs(12 * math.sin(x))))
# определяем, где берём переменные
    x_element = browser.find_element(By.ID, "input_value")
    x = float(x_element.text)
    y = calc(x)

    # вводим получившуюся переменную y в поле ввода
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
# кликаем чек-бокс
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    # скроллим до кнопки
    button = browser.find_element(By.TAG_NAME, "button")
    # browser.execute_script("window.scrollBy(0, 100);") #команда для скролла на опр кол-во пикселей
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)  # команда для скролла до опр элемента
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button) --- прокручивает вниз
    # browser.execute_script("return arguments[0].scrollIntoView(false);", button) --- прокручивает вверх

    # кликаем радиокнопку
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

# кликаем кнопку "Submit"
    button.click() # можно использовать метод .submit() вместо .click(), в этом случае кнопка нажмется даже если она скрыта

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# ссылка на урок https://stepik.org/lesson/228249/step/6?unit=200781
