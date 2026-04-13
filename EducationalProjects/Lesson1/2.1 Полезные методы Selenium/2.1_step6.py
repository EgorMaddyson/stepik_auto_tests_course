from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # находим чек-бокс с текстом "People rule"
    people_radio = browser.find_element(By.ID, "peopleRule")

    # находим атрибут "checked" с помощью встроенного метода get_attribute и проверим его значение:
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    """ та же проверка другим способом, сравнив строки:
    assert people_checked == "true", "People radio is not selected by default """

    # применяем тот же метод get_attribute ко второму radiobutton, и убеждаемся, что атрибут отсутствует
    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None

    # кликаем кнопку "Submit"
    time.sleep(11)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_checked = button.get_attribute("disabled")
    assert button_checked == "true"

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# ссылка на урок https://stepik.org/lesson/165493/step/6?unit=140087
