from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(a, b):
        return str(a + b)


    a_element = browser.find_element(By.ID, "num1")
    b_element = browser.find_element(By.ID, "num2")

    a_value = int(a_element.text)
    b_value = int(b_element.text)
    y_sum = calc(a_value, b_value)

    select_element = (browser.find_element(By.ID, "dropdown"))
    select_element.click()
    select = Select(select_element)
    select.select_by_value(y_sum)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# ссылка на урок https://stepik.org/lesson/228249/step/3?unit=200781
