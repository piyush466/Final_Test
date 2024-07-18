import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

#name
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#firstName"))).send_keys("piyush")
#lastname
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#lastName"))).send_keys("dravyakar")
#email
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#userEmail"))).send_keys("piyush@gmail.com")
#radiobtn
element = driver.find_element(By.CSS_SELECTOR, "#gender-radio-1")
driver.execute_script("arguments[0].click();", element)
driver.execute_script("arguments[0].scrollIntoView();", element)
#number
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#userNumber"))).send_keys("8411878794")

#birthdate
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#dateOfBirthInput"))).click()
months = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select[class='react-datepicker__month-select']")))
select = Select(months)
select.select_by_visible_text("September")

#year
years = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select[class='react-datepicker__year-select']")))
yselect = Select(years)
yselect.select_by_visible_text("2025")
driver.execute_script("arguments[0].scrollIntoView();", years)

#datesi
date = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='20']")))
date.click()

#subjects
subjects = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#subjectsInput")))
subjects.send_keys("Maths")
subjects.send_keys(Keys.ENTER)
#hobbie
hobbies = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")))
hobbies.click()

#images uploads
file_path = "/Users/user/PycharmProjects/pytest_framework/pythonProject/screenshot/screenshot_20240717-184023.png"
upload_picture = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#uploadPicture")))
driver.execute_script("arguments[0].scrollIntoView();", upload_picture)
upload_picture.send_keys(file_path)

#current address
current_address = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#currentAddress")))
current_address.send_keys("Surat")
#states
states = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#react-select-3-input")))
states.send_keys("NCR")
states.send_keys(Keys.ENTER)

#city
cities = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#react-select-4-input")))
cities.send_keys("Delhi")
cities.send_keys(Keys.ENTER)

#submit
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#submit"))).click()
time.sleep(5)
