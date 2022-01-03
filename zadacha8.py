from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

button1 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'$100'))
button2 = browser.find_element_by_id('book')
button2.click()

element_x = browser.find_element_by_id('input_value')
x = element_x.text

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

input3 = browser.find_element_by_id('answer')
input3.send_keys(y)

button1 = browser.find_element_by_id('solve')
button1.click()
