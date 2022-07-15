from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import smtplib
import time
import os
import ssl
from email.message import EmailMessage

Path = "C:\Program Files (x86)\chromedriver.exe"
sender = os.environ.get('Gmail')
password = os.environ.get('Gmail_Key')


class DiscordSpam:
    def __init__(self, email, password, person, wait_time, amount_of_messages, message):
        self.email = email
        self.password = password
        self.person = person
        self.wait_time = wait_time
        self.amount_of_messages = amount_of_messages
        self.message = message

    def spam_messages(self):
        driver = webdriver.Chrome(Path)
        action = ActionChains(driver)
        driver.get("https://discord.com/login")
        search = driver.find_element(By.NAME, "email")
        search.send_keys(self.email)
        search = driver.find_element(By.NAME, "password")
        search.send_keys(self.password)
        search.send_keys(Keys.RETURN)
        time.sleep(5)
        search = driver.find_element(By.CLASS_NAME, "searchBarComponent-3N7dCG").click()
        action.send_keys(self.person).perform()
        time.sleep(1)
        action.send_keys(Keys.ENTER).perform()
        time.sleep(1)
        action.send_keys(Keys.TAB).perform()
        for i in range(self.amount_of_messages):
            action.send_keys(self.message).perform()
            action.send_keys(Keys.ENTER).perform()
            time.sleep(self.wait_time)
        driver.quit()

discord_spam = DiscordSpam(
                input("Enter your email: "),    
                input("Enter your password: "), 
                input("Enter the person/the server you want to spam: "), 
                int(input("Enter the cooldown time: ")), 
                int(input("Enter the amount of messages: ")), 
                input("Enter the message: "))

discord_spam.spam_messages()
