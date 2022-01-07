import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Disable web notifications
my_options = Options()
my_options.set_preference("dom.webnotifications.enabled", False)

geckodriver_path = 'C:/Users/Public/drivers/geckodriver'
browser = webdriver.Firefox(executable_path=geckodriver_path, options=my_options)


browser.get('https://www.decathlon.tw/zh/series/#s3')
#browser.save_screenshot('screenshot.png')

# Click to close pop-up window
btnElem = browser.find_element_by_class_name('closeBtn')

if btnElem.is_displayed() and btnElem.is_enabled():
    btnElem.click()
    
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME,"closeBtn"))).click()
"""
#  Go to 聯絡我們
linkElem = browser.find_element_by_link_text('客服信箱')
linkElem.click()

time.sleep(5) # seconds

browser.get('http://taipeiads.com')
browser.find_element_by_id('policy-close').click()
html = browser.page_source
time.sleep(3) # seconds
browser.quit()

soup = BeautifulSoup(html, "html.parser")
title = soup.select('head > title')[0]
print(title.getText())

