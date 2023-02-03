
import time, sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
action = ActionChains(driver)

driver.get("https://www.google.com/intl/en-GB/gmail/about/")
time.sleep(1)

signin_button = driver.find_element(By.XPATH, '/html/body/header/div/div/div/a[2]')
action.click(on_element = signin_button).perform()
time.sleep(2)

email_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
email_element.send_keys("seleniumJackson2004@gmail.com")
next_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')
action.click(on_element = next_button).perform()
time.sleep(2)

password_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
password_element.send_keys("seleniumtesting2004#$@")
next1_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[3]')
action.click(on_element = next1_button).perform()
time.sleep(2)

compose_button = driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div/div')
action.click(on_element = compose_button).perform()
time.sleep(5) 

send_email = driver.find_element(By.XPATH, '/html/body/div[24]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[1]/td[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/input')
action.click(on_element = send_email).perform()
send_email.send_keys(sys.argv[1])
time.sleep(10)

message = ""
for i in range(2, len(sys.argv)):
    message += sys.argv[i] + ' '

message_area = driver.find_element(By.XPATH, '/html/body/div[24]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/div[1]/div[2]/div[3]/div/table/tbody/tr/td[2]/div[2]/div')
message_area.send_keys(message)
time.sleep(10)

send_button = driver.find_element(By.XPATH, '/html/body/div[24]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[1]/div/div[2]/div[1]')
action.click(on_element = send_button).perform()

