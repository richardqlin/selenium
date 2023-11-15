from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.add_experimental_option('prefs',{'download.default_directory':'C:/Downloads'})

driver = webdriver.Chrome(executable_path='C:/Users/Richard/Downloads/chromedriver_win32/chromedriver.exe')

driver.get('http://demo.automationtesting.in/FileDownload.html')
driver.maximize_window()

#download text file

driver.find_element_by_id('textbox').send_keys('testing download text file')

driver.find_element_by_id('createTxt').click() # Generator text file button

driver.find_element_by_id('link-to-download').click() # Download link

driver.find_element_by_id('pdfbox').send_keys('testing pdf file')

driver.find_element_by_id('createPdf').click() # Generator pdf file button

driver.find_element_by_id('pdf-link-to-download').click() # Download link


#driver.close()