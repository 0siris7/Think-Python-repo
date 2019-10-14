from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("/usr/bin/chromedriver")
driver.get("https://web.whatsapp.com")
wait = WebDriverWait(driver, 600)
target = '"Adarsh"' #Friends name
string = "Greetings traveler , for this is an automated message"
x_args = '//span[contains(@title, ' + target + ')]'
target = wait.until(ec.presence_of_element_located((By.XPATH,x_args)))
target.click()
input_box = driver.find_element_by_class_name('_13mgZ')
for i in range(50):
    input_box.send_keys(string + Keys.ENTER)
