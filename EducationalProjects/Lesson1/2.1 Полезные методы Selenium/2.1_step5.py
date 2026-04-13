from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # функция расчёта значения переменной для дальнейшего ввода в поле
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    # определяем, где берём переменные
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # вводим получившуюся переменную y в поле ввода
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    # кликаем чек-бокс
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click()

    # кликаем радиокнопку
    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option2.click()

    # кликаем кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# ссылка на урок https://stepik.org/lesson/165493/step/5?unit=140087
