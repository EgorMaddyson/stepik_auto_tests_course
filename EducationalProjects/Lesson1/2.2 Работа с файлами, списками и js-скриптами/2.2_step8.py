from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
# current_dir = os.path.abspath(os.path.dirname(__file__)) # если тест и файл в одной директории
directory = "D:/Yandex_Download/test_pic" # если тест и файл в разных директориях (лучше использовать обратный слеш "/")
file_name = "test.txt"
file_path = os.path.join(directory, file_name)

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Ivanov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("test@test.com")
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# ссылка на урок https://stepik.org/lesson/228249/step/8?unit=200781
