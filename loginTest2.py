from selenium import webdriver

from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(4)

URL = "https://rahulshettyacademy.com/loginpagePractise/"

driver.get(URL)
driver.maximize_window()

driver.find_element(By.ID,"username").send_keys("rahulshettyacademy")
driver.find_element(By.ID, "password").send_keys("learning")
driver.find_element(By.CSS_SELECTOR,"span.text-white.termsText").click()
driver.find_element(By.ID, "signInBtn").click()