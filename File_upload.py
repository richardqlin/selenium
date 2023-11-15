from selenium import webdriver


import time
driver = webdriver.Chrome(executable_path='C:/Users/Richard/Downloads/chromedriver_win32/chromedriver.exe')

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

driver.switch_to_frame(0)

driver.find_element_by_xpath('//*[@id="RESULT_FileUpload-10"]').send_keys('C:/Users/richardlin/Pictures/Saved Pictures/apple.jpg')

