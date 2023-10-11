from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    image = browser.find_element(By.ID, "treasure")
    x_element = image.get_attribute("valuex")
    y = calc(x_element)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    check = browser.find_element(By.ID, "robotCheckbox")
    check.click()

    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit.click()

finally:
    time.sleep(30)
    browser.quit()
