from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input_y = browser.find_element(By.ID, "answer")
    input_y.send_keys(y)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

# ссылка на урок https://stepik.org/lesson/184253/step/6?unit=158843
