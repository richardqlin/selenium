from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome(executable_path='C:/Users/Richard/Downloads/chromedriver_win32/chromedriver.exe')


driver.get('http://demo.automationtesting.in/Windows.html')

driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()


print(driver.current_window_handle)

handles = driver.window_handles # returns all the handle values of opened browser windows

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title=='Frames & windows':
        driver.close()
    time.sleep(3)

#driver.quit()
