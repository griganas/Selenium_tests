
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions, wait
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(4)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")


URL = "https://rahulshettyacademy.com/"
driver.get(URL)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
time.sleep(10)

driver.get_screenshot_as_file("screen.png")
