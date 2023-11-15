from selenium import webdriver
from selenium.webdriver import ActionChains

import time
driver = webdriver.Chrome(executable_path='C:/Users/Richard/Downloads/chromedriver_win32/chromedriver.exe')

driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
driver.maximize_window()

source_element_1 =driver.find_element_by_xpath('//*[@id="box6"]')

target_element_1 = driver.find_element_by_xpath('//*[@id="box106"]')

actions = ActionChains(driver)

actions.drag_and_drop(source_element_1,target_element_1).perform()

source_element_2 = driver.find_element_by_id('box7')

target_element_2= driver.find_element_by_xpath('//*[@id="box107"]')

actions.drag_and_drop(source_element_2,target_element_2).perform()


source_element_3= driver.find_element_by_id('box3')


target_element_3= driver.find_element_by_id('box103')

actions.drag_and_drop(source_element_3,target_element_3).perform()