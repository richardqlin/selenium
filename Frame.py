from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
driver = webdriver.Chrome(executable_path='C:/Users/Richard/Downloads/chromedriver_win32/chromedriver.exe')

driver.get('https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html')


driver.switch_to.frame('packageListFrame')  # the first frame

driver.find_element_by_link_text('org.openqa.selenium').click()

time.sleep(3)

driver.switch_to.default_content()

driver.switch_to.frame('packageFrame') # the second frame

driver.find_element_by_link_text('WebDriver').click()

time.sleep(3)


driver.switch_to.default_content()

time.sleep(3)
driver.switch_to.frame('classFrame')

driver.find_element_by_xpath('/html/body/header/nav/div[1]/div[1]/ul/li[6]').click()





