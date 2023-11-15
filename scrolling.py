from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
driver = webdriver.Chrome(executable_path='C:/Users/Richard/Downloads/chromedriver_win32/chromedriver.exe')

driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')

driver.maximize_window() # Maximize Window

# 1. Scroll down page by pixel
#driver.execute_script('window.scrollBy(0,1000)','')

# 2 Scroll down page till the element is visible

#flag = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img')
#driver.execute_script('arguments[0].scrollIntoView();',flag)

# 3. scroll down page till end

driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')







