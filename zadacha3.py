from selenium import webdriver
import math

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id('num1')
x = x_element.text
y_element = browser.find_element_by_id('num2')
y = y_element.text

def sum(x,y):
    str(int(x) + int(y))

z =  sum(x,y)

element2 = browser.find_element_by_id('dropdown').send_keys(str(int(x) + int(y)))
element3 = browser.find_element_by_css_selector('.btn').click()
