from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

Path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(Path)
action = ActionChains(driver)

def spam_messages(person, wait_time, amount_of_messages, message):
    driver.get("https://discord.com/login")
    search = driver.find_element(By.NAME, "email")
    search.send_keys("email")
    search = driver.find_element(By.NAME, "password")
    search.send_keys("password")
    search.send_keys(Keys.RETURN)
    time.sleep(5)
    search = driver.find_element(By.CLASS_NAME, "searchBarComponent-3N7dCG").click()
    action.send_keys(person).perform()
    time.sleep(1)
    action.send_keys(Keys.ENTER).perform()
    time.sleep(1)
    action.send_keys(Keys.TAB).perform()
    for i in range(amount_of_messages):
        action.send_keys(message).perform()
        action.send_keys(Keys.ENTER).perform()

spam_messages(input("Enter the person: "), int(input("Enter the cooldown: ")), int(input("Enter the amount of messages: ")), input("Enter the message: "))