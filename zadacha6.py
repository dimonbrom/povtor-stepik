from selenium import webdriver
import math

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_css_selector('.btn')
input1.click()

confirm = browser.switch_to.alert
confirm.accept()

element_x = browser.find_element_by_id('input_value')
x = element_x.text

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

input3 = browser.find_element_by_id('answer')
input3.send_keys(y)

button1 = browser.find_element_by_css_selector('.btn')
button1.click()
