import XLUtils

import time
import openpyxl
from selenium.webdriver.common.keys import Keys

from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/Richard/Downloads/chromedriver_win32/chromedriver.exe')

driver.get('https://opensource-demo.orangehrmlive.com')
driver.maximize_window() # maximize page
from xls2xlsx import XLS2XLSX
x2x = XLS2XLSX("C:/Users/richardlin/Downloads/Login1.xls")
x2x.to_xlsx("C:/Users/richardlin/Downloads/Login1.xlsx")

path ='C:/Users/richardlin/Downloads/Login1.xlsx'

rows = XLUtils.getRowCount(path,'Sheet1')

for r in range(2,rows+1):
    username = XLUtils.readData(path,'Sheet1',r,1)
    password = XLUtils.readData(path,'Sheet1',r,2)

    driver.find_element_by_id('txtUsername').send_keys(username)
    driver.find_element_by_id('txtPassword').send_keys(password)
    driver.find_element_by_id('btnLogin').click()
    time.sleep(1)
    print(driver.current_url,username,password)


    if driver.current_url =='https://opensource-demo.orangehrmlive.com/index.php/dashboard':
        print('test is passed')
        XLUtils.writeData(path,'Sheet1',r,3,'test passed')
    else:
        print('test failed')
        XLUtils.writeData(path, 'Sheet1', r, 3, 'test failed')
    #driver.back()
    #driver.find_element_by_link_text('')
    driver.execute_script("window.history.go(-1)")
    driver.find_element_by_id('txtUsername').clear()










