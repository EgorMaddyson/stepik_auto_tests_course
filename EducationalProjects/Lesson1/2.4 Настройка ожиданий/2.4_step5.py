from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.implicitly_wait(5) # говорим WebDriver искать каждый элемент в течение 5 секунд, по умолчанию опрос каждые 500 мс
browser.get("http://suninjuly.github.io/wait1.html")
button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")
assert "successful" in message.text

# Ожидаем до 10 сек, но проверяем каждые 0.2 сек (200 мс)
# wait = WebDriverWait(driver, timeout=10, poll_frequency=0.2)
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
# element = wait.until(EC.presence_of_element_located((By.ID, "myElement")))

# ссылка на урок https://stepik.org/lesson/181384/step/5?unit=156009
