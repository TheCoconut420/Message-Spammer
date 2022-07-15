from argparse import Action
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

Path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(Path)
action = ActionChains(driver)

def youtube_viewer(link, wait_time, amount_of_views):
    for i in range(amount_of_views):
        driver.get(link)
        time.sleep(wait_time)


youtube_viewer(input("Enter the link: "), int(input("Enter the wait time: ")), int(input("Enter the amount of views: ")))
driver.quit()