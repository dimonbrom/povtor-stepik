from selenium import webdriver
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_name('firstname').send_keys('Di')
input2 = browser.find_element_by_name('lastname').send_keys('Tr')
input3 = browser.find_element_by_name('email').send_keys('ru')


current_dir = os.path.abspath(os.path.dirname('__file__'))    
file_path = os.path.join(current_dir, 'test.txt')
element1 = browser.find_element_by_id('file')
element1.send_keys(file_path)

button2 = browser.find_element_by_css_selector('.btn')
#browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
button2.click()
