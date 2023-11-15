from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(executable_path='C:/Users/Richard/Downloads/chromedriver_win32/chromedriver.exe')

driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?15377059607')

# how to finde how many inputboxes present in web

inputboxes = driver.find_elements(By.CLASS_NAME,'text_field')

print(len(inputboxes))



# input
status = driver.find_element_by_id('RESULT_TextField-1').is_displayed()

print('Displayed or not',status)

status = driver.find_element_by_id('RESULT_TextField-1').is_enabled()

print('Enabled or not',status)

driver.find_element_by_id('RESULT_TextField-1').send_keys('richard')

driver.find_element_by_id('RESULT_TextField-2').send_keys('lin')

driver.find_element_by_id('RESULT_TextField-3').send_keys('333-322-1213')

driver.find_element_by_id('RESULT_TextField-4').send_keys('USA')

driver.find_element_by_id('RESULT_TextField-5').send_keys('Fremont')

driver.find_element_by_id('RESULT_TextField-6').send_keys('richardqlin@gmail.com')


# radio button
status = driver.find_element_by_name('RESULT_RadioButton-7').is_selected()

print(status)


driver.find_element_by_xpath ('// *[ @ id = "q26"] / table / tbody / tr[1] / td').click()

status = driver.find_element_by_id('RESULT_RadioButton-7_0').is_selected()

print(status)


#  checkbox

driver.find_element_by_xpath('//*[@id="q15"]/table/tbody/tr[1]/td').click()


driver.find_element_by_xpath('//*[@id="q15"]/table/tbody/tr[6]/td').click()

# select option

element = driver.find_element_by_id('RESULT_RadioButton-9')

drp= Select(element)
# select by visible text
#drp.select_by_visible_text('Morning') # Morninig


# select by index

#drp.select_by_index(2) # Afternoon

# select by value

drp.select_by_value('Radio-2') # Evening

# count number of options

print(len(drp.options))

# capture all the options and print them as output

all_options = drp.options

for option in all_options:
    print(option.text)



