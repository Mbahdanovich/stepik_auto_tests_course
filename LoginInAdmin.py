import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time.sleep(5)

driver.get("https://space.a-mates.com/login")
time.sleep(5)

email_field = driver.find_element(By.CLASS_NAME, "MuiInputBase-input.MuiOutlinedInput-input")
email_field.send_keys("demo@a-mates.com")
time.sleep(5)

password_field = driver.find_element(By.CLASS_NAME, "MuiInputBase-input.MuiOutlinedInput-input.MuiInputBase-inputAdornedEnd.MuiOutlinedInput-inputAdornedEnd")
password_field.send_keys("Orange609!")
time.sleep(5)

signIn_button = driver.find_element(By.CLASS_NAME, "MuiButtonBase-root.MuiButton-root.MuiButton-contained.jss19")
signIn_button.click()
time.sleep(5)

user_name = driver.find_element(By.CLASS_NAME, "jss40")
user_name_text = user_name.text

assert "demo@a-mates.com" == user_name_text

driver.quit()
