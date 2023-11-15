import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/Richard/Downloads/chromedriver_win32_2/chromedriver.exe')

driver.get('http://ww7.demoaut.com/mercurywelcome.php')

#driver.save_screenshot('C:/Users/Richard/Downloads/homepage.png')

driver.get_screenshot_as_file('C:/Users/Richard/Downloads/homepage2.jpg')