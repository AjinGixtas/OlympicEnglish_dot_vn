# Scraper Bot

## Purpose
# This tool is designed for educational purposes to demonstrate web scraping 
# techniques. It should be used responsibly and in compliance with legal and 
# ethical guidelines.

## Disclaimer
# This tool is provided for educational purposes only. The author does not 
# endorse or take responsibility for any misuse of this tool. Users are 
# responsible for ensuring their actions comply with all applicable laws and 
# regulations.

## Usage Instructions
# You need to create an olympicenglish.vn account and openai.com account
# All library must be installed manually along with the Python interpeter and the 
# headless browser selenium
# Run the script by run "py script.py" in the directory holding this script

## Ethical Guidelines
# - Do not use this tool to scrape personal or sensitive information.
# - Do not use this tool to engage in spamming or any other illegal activities.
# - Respect website terms of service and robots.txt files.

## Account Creation
# The bot may interact with various websites, some of which may require account 
# creation. Note that:
# - Some websites may not have anti-bot countermeasures. Even in the absence of 
# these measures, users must adhere to ethical practices and website terms of 
# service.
# - Use the bot to create accounts only where it is legal and ethical to do so.
# - Avoid using the bot to create multiple accounts on any platform to prevent 
# abuse and potential legal consequences.

## FAQ
# Q: The script doesn't work!
# A: That's not a question, moreover, it works on my end, and that's what 
#    matter (Sorry that was rude)
# Q: Is this a virus?
# A: Yes.
# Q: Instruction doesn't work anymore.
# A: The instruction is last updated at 01/07/2024 01:32:48 (dd/mm/yyyy hh:mm:ss)

## Note:
# - In websites that are known to have anti-bot countermeasures, the bot have an 
# unconditional delay of 45 second is used to allow user manually resolve it for 
# the bot. The user must resolve it in 45 second or the bot will brick. I can fix 
# it, but I won't.

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
if __name__ == '__main__':
    # My super secret info, no peaking (>.<)
    
    # The olympicenglish.vn registered account's credential goes here
    PHONE_NUMBER = '09XXXXXXXX'
    PASSWORD = 'password'
    # The ChatGPT registered account's credential goes here
    OAI_EMAIL = 'user@example.com'
    OAI_PASSWORD = 'password'
    OAI_CHAT_CHANNEL = 'https://chatgpt.com/c/XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
    
    options = uc.ChromeOptions()
    driver1 = uc.Chrome(options=options, use_subprocess=False)
    driver1.get('https://chatgpt.com/auth/login')
    time.sleep(45)
    driver1.find_elements(By.CLASS_NAME, 'btn-secondary')[0].click()
    time.sleep(2 + random.random())
    driver1.find_element(By.CLASS_NAME, 'email-input').send_keys(OAI_EMAIL)
    time.sleep(random.random())
    driver1.find_element(By.CLASS_NAME, 'continue-btn').click()
    time.sleep(1 + random.random() * .2)
    driver1.find_element(By.ID, 'password').send_keys(OAI_PASSWORD)
    time.sleep(1 + random.random() * .2)
    driver1.find_element(By.CLASS_NAME, '_button-login-password').click()
    time.sleep(45)
    driver1.get(OAI_CHAT_CHANNEL)
    time.sleep(5 + random.random() * 2)
    prompt_field = driver1.find_element(By.ID, 'prompt-textarea')
    submit_button = driver1.find_elements(By.CLASS_NAME, 'transition-colors')[1]
    prompt = 'Just respond with the letter correspond to the answer. ONLY THAT LETTER. NOTHING ELSE.\n'
    prompt_field.send_keys(prompt)
    time.sleep(random.random() * .1)
    submit_button.click()
    driver = webdriver.Chrome()
    driver.get("https://olympicenglish.vn/Olympic/Account/Login")
    time.sleep(5 + random.random())
    driver.find_element(By.ID, 'lUserName').send_keys(PHONE_NUMBER)
    driver.find_element(By.ID, 'lPassword').send_keys(PASSWORD)
    driver.find_element(By.CLASS_NAME, 'btn-success').click()
    driver.get("https://olympicenglish.vn/batdauvong1")
    time.sleep(5 + random.random())
    driver.find_element(By.CLASS_NAME, 'btn-lg').click()

    for i in range(30):
        j = 0
        time.sleep(random.random() * 3 + 3.5)
        try:
            Header = driver.find_elements(By.CLASS_NAME, 'ng-binding')[1]
            Sentence = driver.find_elements(By.CLASS_NAME, 'ng-binding')[2]
            tug = driver.find_elements(By.CLASS_NAME, 'ng-binding')[3]
            A = driver.find_elements(By.CLASS_NAME, 'grammar-cursor')[0]
            B = driver.find_elements(By.CLASS_NAME, 'grammar-cursor')[1]
            C = driver.find_elements(By.CLASS_NAME, 'grammar-cursor')[2]
            D = driver.find_elements(By.CLASS_NAME, 'grammar-cursor')[3]
            prompt = Header.text + '\n' + Sentence.get_attribute('innerHTML').encode('utf-8') + '\n' + tug.text + ' \n A - ' + A.text + ' \n B - ' + B.text + ' \n C - ' + C.text + ' \n D - ' + D.text
            prompt_field.send_keys(prompt)
            time.sleep(1 + random.random() * 2)
            submit_button.click()
            output = driver.find_elements(By.CLASS_NAME, 'markdown')[i+1].find_element(By.TAG_NAME, 'p').text
            if output == 'A':
                A.click()
            elif output == 'B':
                B.click()
            elif output == 'C':
                C.click()
            elif output == 'D':
                D.click()
        # Fail safe measure :/
        except Exception as e:
            print(e)
            A.click()