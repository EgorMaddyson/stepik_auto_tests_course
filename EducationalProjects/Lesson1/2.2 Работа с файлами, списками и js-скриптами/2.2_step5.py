from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"

browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
# browser.execute_script("window.scrollBy(0, 100);") #команда для скролла на опр кол-во пикселей
browser.execute_script("return arguments[0].scrollIntoView(true);", button) #команда для скролла до опр элемента
# browser.execute_script("return arguments[0].scrollIntoView(true);", button) --- прокручивает вниз
# browser.execute_script("return arguments[0].scrollIntoView(false);", button) --- прокручивает вверх
button.click() # можно использовать метод .submit() вместо .click(), в этом случае кнопка нажмется даже если она скрыта

# ссылка на урок https://stepik.org/lesson/228249/step/5?unit=200781
