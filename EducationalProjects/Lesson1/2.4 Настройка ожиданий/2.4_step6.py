from selenium import webdriver
from selenium.webdriver.common.by import By
"""
!!! ПРИМЕР ИСПОЛЬЗОВАНИЯ ОЖИДАНИЯ С ОПРОСОМ В 200 МС

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
# ниже говорим WebDriver искать каждый элемент в течение 5 секунд
wait = WebDriverWait(browser, timeout=10, poll_frequency=0.2)
browser.get("https://suninjuly.github.io/cats.html")

try:
    button = wait.until(
        EC.element_to_be_clickable((By.TAG_NAME, "button"))
    )
    button.click()
finally:
    browser.quit()
"""
# ниже решение дял получения ожидаемой ошибки по уроку:
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/cats.html")

try:
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    import time
    time.sleep(1)
    browser.quit()

# ссылка на урок https://stepik.org/lesson/181384/step/6?unit=156009
