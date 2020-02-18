from selenium import webdriver
from time import sleep

from secrets import phone_number


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(15)

        login_btn = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/div[1]/button')
        login_btn.click()
        sleep(2)

        phone_in = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div[2]/div[2]/div/input')
        phone_in.send_keys('7798467447')
        sleep(2)

        login_btn = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div[2]/button')
        login_btn.click()
        sleep(20)
        # OTP
        continue_btn = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div[2]/button')
        continue_btn.click()

        sleep(2)
        popup_1 = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()
        sleep(2)
        popup_2 = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()
        sleep(2)

    def like(self):
        like_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(2)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()


bot = TinderBot()
bot.login()
bot.auto_swipe()
