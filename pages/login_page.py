from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_file import Base


class Login(Base):
    username = (By.ID, "username")
    password = (By.ID, "password")
    submit_btn = (By.ID, "submit")
    after_login_succesful_text = (By.CSS_SELECTOR, "h1[class='post-title']")
    Invalid_creds = (By.CSS_SELECTOR, "div[id='error']")

    def do_login(self,username, password):
        try:
            self.send_key(self.username, username)
            self.send_key(self.password , password)
            self.do_click(self.submit_btn)
        except:
            raise
