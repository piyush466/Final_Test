import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.google.co.in/")
driver.implicitly_wait(10)
driver.maximize_window()
wait = WebDriverWait(driver,10)
search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#APjFqb")))
search.send_keys("amazon")
search.send_keys(Keys.ENTER)

time.sleep(3)


