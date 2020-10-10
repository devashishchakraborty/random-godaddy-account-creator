#! Python3
# create_account.py - A simple useless Python Script to open the browser and create a Godaddy Account with a temporary email using the Selenium Module.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip
import time


class CreateAccount:

    def __init__(self, username):
        self.username = username
        self.email = ""
        self.password = ""
        self.driver = webdriver.Firefox()

    def copy_password(self):
        self.driver.get("https://1password.com/password-generator/")
        time.sleep(2)
        add_symbols = self.driver.find_element_by_id("symbols")
        add_symbols.click()
        copy_pass = self.driver.find_element_by_id("copy-secure-password")
        copy_pass.click()
        self.password = pyperclip.paste()
        time.sleep(2)

    def copy_email(self):
        self.driver.get("https://temp-mail.org/en/")
        time.sleep(2)
        copy_mail = self.driver.find_element_by_id("click-to-copy")
        copy_mail.click()
        self.email = pyperclip.paste()
        time.sleep(2)

    def sign_up(self):
        self.driver.get("https://sso.godaddy.com/account/create?realm=idp&")
        time.sleep(2)
        email = self.driver.find_element_by_id("email")
        user = self.driver.find_element_by_id("username")
        pw = self.driver.find_element_by_id("new-password")
        submit_button = self.driver.find_element_by_id("submitBtn")
        user.send_keys(str(self.username))
        time.sleep(1)
        email.send_keys(str(self.email))
        time.sleep(1)
        pw.send_keys(str(self.password))
        time.sleep(1)
        submit_button.click()

    def execute(self):
        self.copy_password()
        self.copy_email()
        self.sign_up()


username = "RandomUsernamegerfvvfge"
acc = CreateAccount(username)
acc.execute()
