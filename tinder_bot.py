# Write your code here :-)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time


driver_path = "/Applications/chromedriver"

class TinderBot():
    def __init__(self):
        self.driver=webdriver.Chrome("/Applications/chromedriver")

    def login(self):
        self.driver.get('https://tinder.com')

        time.sleep(2)

        login_btn = self.driver.find_element(By.XPATH, '//*[@id="c464932099"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')  
        login_btn.click()
        
        window_before = self.driver.window_handles[0]
        
         # click 'I agree' and facebook button
        agree_btn = self.driver.find_element(By.XPATH, '//*[@id="c464932099"]/div/div[2]/div/div/div[1]/div[1]/button')
        agree_btn.click()
        
        time.sleep(5)

        fb_btn = self.driver.find_element(By.XPATH, '//*[@id="c-1263448977"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
        fb_btn.click() 

        time.sleep(2)

        for handle in self.driver.window_handles:
            if handle != window_before:
                login_page = handle

        time.sleep(7)

        self.driver.switch_to.window(login_page)

        time.sleep(3)
        # switch to window 
        # window_after = driver.window_handles[1]
        # driver.switch_to.window(window_after)

        email_in = self.driver.find_element(By.XPATH, '//*[@id="email"]')   
        email_in.click()
        email_in.send_keys('ENTER EMAIL')

        pw_in = self.driver.find_element(By.XPATH, '//*[@id="pass"]')
        pw_in.send_keys('ENTER PASS')

        login_btn = self.driver.find_element(By.XPATH, '//*[@id="loginbutton"]')
        login_btn.click()

        time.sleep(3)

        self.driver.switch_to.window(window_before)

        popup_1 = self.driver.find_element(By.XPATH, '//*[@id="c-1263448977"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        popup_2 = self.driver.find_element(By.XPATH, '//*[@id="c-1263448977"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

    def like(self):
        like_btn = self.driver.find_element(By.XPATH, '//*[@id="c464932099"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button') 
        like_btn.click() 

    def dislike(self):
        dislike_btn = self.driver.find_element(By.XPATH, '//*[@id="c464932099"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            time.sleep(0.5)
            # try:
            self.like()
            # except Exception:
            #     try:
            #         self.close_popup()
            #     except Exception:
            #         self.close_match()

    def close_popup(self):
        popup_3 = self.driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element(By.XPATH, '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

bot = TinderBot()
bot.login()
bot.auto_swipe()
