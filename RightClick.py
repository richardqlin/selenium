from selenium import webdriver
from selenium.webdriver import ActionChains

import time
driver = webdriver.Chrome(executable_path='C:/Users/Richard/Downloads/chromedriver_win32/chromedriver.exe')


driver.get('http://swisnl.github.io/jQuery-contextMenu/demo.html')

button = driver.find_element_by_xpath('/html/body/div/section/div/div/div/p/span')

actions = ActionChains(driver)

actions.context_click(button).perform()
