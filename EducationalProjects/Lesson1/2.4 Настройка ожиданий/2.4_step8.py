from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

browser = webdriver.Chrome()
# ниже говорим WebDriver искать каждый элемент в течение 12 секунд, с опросом 100 мс
wait = WebDriverWait(browser, timeout=12, poll_frequency=0.1)
browser.get("http://suninjuly.github.io/explicit_wait2.html")
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Ждём, пока в элементе с id="price" не появится текст "$100"
    wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button1 = browser.find_element(By.ID, "book")
    button1.click()
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input_y = browser.find_element(By.ID, "answer")
    input_y.send_keys(y)
    button2 = browser.find_element(By.ID, "solve")
    button2.submit()

finally:
    import time
    time.sleep(5) # для записи результата
    browser.quit()

# ссылка на урок https://stepik.org/lesson/181384/step/8?unit=156009
