from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(4)

URL = "https://rahulshettyacademy.com/loginpagePractise/"

driver.get(URL)
driver.maximize_window()

driver.find_element(By.ID,"username").send_keys("rahulshetty")
driver.find_element(By.ID, "password").send_keys("learning")
driver.find_element(By.CSS_SELECTOR,"span.text-white.termsText").click()
driver.find_element(By.ID, "signInBtn").click()


wait = WebDriverWait(driver,2)

try:
    wait.until(EC.title_is("ProtoCommerce"))
    print("Login successful!")
except:
    print("Login failed! Capturing screenshot...")
    driver.save_screenshot("login_error.png")
    error_message = driver.find_element(By.CSS_SELECTOR, ".alert-danger").text
    print("Error Message:", error_message)