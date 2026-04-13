from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait2.html")
# ниже говорим WebDriver искать каждый элемент в течение 5 секунд, с опросом 100 мс
#wait = WebDriverWait(browser, timeout=5, poll_frequency=0.1)
try:
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:
    browser.quit()

# ссылка на урок https://stepik.org/lesson/181384/step/7?unit=156009

"""
Если мы захотим проверять, что кнопка становится неактивной после отправки данных, то можно задать негативное правило с помощью метода until_not:

# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
button = WebDriverWait(browser, 5).until_not(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
"""

"""
browser.implicitly_wait(5)
try:
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:
    browser.quit()
"""
