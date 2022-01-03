from selenium import webdriver
import math

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
element_x = browser.find_element_by_id('treasure')
x = element_x.get_attribute('valuex')

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

element1 = browser.find_element_by_id("answer").send_keys(y)
element2 = browser.find_element_by_id("robotCheckbox").click()
element3 = browser.find_element_by_id("robotsRule").click()
element4 = browser.find_element_by_css_selector(".btn").click()
