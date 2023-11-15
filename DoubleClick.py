from selenium import webdriver
from selenium.webdriver import ActionChains

import time
driver = webdriver.Chrome(executable_path='C:/Users/Richard/Downloads/chromedriver_win32/chromedriver.exe')

driver.get('https://testautomationpractice.blogspot.com/')

driver.maximize_window() # maximize page

element = driver.find_element_by_xpath('//*[@id="HTML10"]/div[1]/button')

actions = ActionChains(driver)

actions.double_click(element).perform() #double click

