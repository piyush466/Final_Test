import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
alert = driver.switch_to.alert
alert.accept()
time.sleep(2)

mouse_hove = driver.find_element(By.CSS_SELECTOR ,"#mousehover")
driver.execute_script("arguments[0].scrollIntoView();", mouse_hove)
time.sleep(2)
action = ActionChains(driver)
action.move_to_element(mouse_hove).perform()

window = driver.find_element(By.CSS_SELECTOR, "#openwindow")
driver.execute_script("arguments[0].scrollIntoView();", window)
window.click()
windows = driver.window_handles
print(windows)
driver.switch_to.window(windows[1])
print(driver.title)