import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

INSTAGRAM = "https://www.instagram.com"
USERNAME = os.environ["username"]
PASSWORD = os.environ["password"]


class InstaFollower:
    def __init__(self):
        chrome_webdriver_path = "C:\chromedriver_win32\chromedriver"
        self.driver = webdriver.Chrome(executable_path=chrome_webdriver_path)

    # open and login to instagram. close all popups as they appear
    def login(self):
        self.driver.get(INSTAGRAM)
        time.sleep(3)
        login = self.driver.find_element(By.CSS_SELECTOR, ".f0n8F input")
        login.send_keys(USERNAME, Keys.TAB, PASSWORD, Keys.ENTER)
        time.sleep(5)
        not_now_button = self.driver.find_element(By.CSS_SELECTOR, ".cmbtv button")
        not_now_button.click()
        time.sleep(4)
        no_notifications_button = self.driver.find_element(By.CLASS_NAME, "HoLwm ")
        no_notifications_button.click()

    # get the followers of any account you want. In this case we use fcbarcelona
    # click on the followers of fcbarcelona, scroll the pop-up bar a few times to load up more followers in the window
    def find_followers(self):
        search_bar = self.driver.find_element(By.CSS_SELECTOR, ".QY4Ed input")
        search_bar.send_keys("fcbarcelona")
        time.sleep(3)
        first_result = self.driver.find_element(By.XPATH,
                                                '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div')
        first_result.click()
        time.sleep(3)
        followers = self.driver.find_element(By.XPATH,
                                             '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div')
        followers.click()
        time.sleep(2)
        scroll = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]')
        for i in range(2):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scroll)
            time.sleep(2)

    # find the follow buttons and follow each person. if you already follow the person,
    # click cancel in the popup and continue
    def follow(self):
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'li button')
        for account in follow_buttons:
            try:
                account.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.CLASS_NAME, "HoLwm")
                cancel_button.click()
            time.sleep(1)
