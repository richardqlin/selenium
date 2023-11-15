from selenium import webdriver
from selenium.webdriver import ActionChains

import time
driver = webdriver.Chrome(executable_path='C:/Users/Richard/Downloads/chromedriver_win32/chromedriver.exe')

driver.get('https://opensource-demo.orangehrmlive.com')

driver.find_element_by_id('txtUsername').send_keys('Admin')


driver.find_element_by_id('txtPassword').send_keys('admin123')

driver.find_element_by_id('btnLogin').click()

admin = driver.find_element_by_id('menu_admin_viewAdminModule')
usermgnt = driver.find_element_by_id('menu_admin_UserManagement')
users = driver.find_element_by_id('menu_admin_viewSystemUsers')

actions = ActionChains(driver)

