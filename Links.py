
from selenium import webdriver

import time

driver = webdriver.Chrome(executable_path='C:/Users/Richard/Downloads/chromedriver_win32/chromedriver.exe')


driver.get('https://www.expedia.com/')

links=driver.find_elements_by_tag_name('a')

print('Numbers of links present',len(links))

'''
for link in links:
    print(link.text)
'''
# clicking on the link

#driver.find_element_by_link_text('See our travel options').click()

driver.find_element_by_partial_link_text('See').click()

