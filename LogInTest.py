
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(4)

URL = "https://rahulshettyacademy.com/loginpagePractise/"

driver.get(URL)
driver.maximize_window()

driver.find_element(By.CLASS_NAME, "blinkingText").click()

windowsOpened = driver.window_handles
window_handles = driver.window_handles
driver.switch_to.window(windowsOpened[1])
print (driver.title)
text = driver.find_element(By.PARTIAL_LINK_TEXT,"mentor@rahulshettyacademy.com").text
print (text)
driver.close()

driver.switch_to.window(windowsOpened[0])

driver.find_element(By.ID,"username").send_keys(text)
driver.find_element(By.ID, "password").send_keys(123456)
driver.find_element(By.CSS_SELECTOR,"span.text-white.termsText").click()
time.sleep(10)
driver.find_element(By.ID, "signInBtn").click()
wait = WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)

