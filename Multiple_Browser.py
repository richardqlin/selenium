from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time
driver = webdriver.Chrome(executable_path='C:/Users/Richard/Downloads/chromedriver_win32/chromedriver.exe')


#driver = webdriver.Ie(executable_path='C:/Users/richardlin/Downloads/IEDriverServer_x64_3.150.1/IEDriverServer.exe')
driver.get('http://newtours.demoaut.com/')

print(driver.title)
print(driver.current_url)
time.sleep(5)
print(driver.page_source)

driver.close()