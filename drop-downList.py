from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1_text = browser.find_element(By.ID, "num1")
    num1 = int(num1_text.text)
    num2_text = browser.find_element(By.ID, "num2")
    num2 = int(num2_text.text)
    x = str(num1 + num2)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(x)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
