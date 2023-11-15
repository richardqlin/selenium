from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
driver = webdriver.Chrome(executable_path='C:/Users/Richard/Downloads/chromedriver_win32/chromedriver.exe')

driver.get('https://testautomationpractice.blogspot.com/')

driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()

time.sleep(5)

driver.switch_to_alert().accept() # close alert window using OK button

#driver.switch_to_alert().dismiss() # close alert window using cancel button




