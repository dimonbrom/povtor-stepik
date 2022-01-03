from selenium import webdriver
import math

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

element_x = browser.find_element_by_id("input_value")
x = element_x.text

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

element1 = browser.find_element_by_id("answer").send_keys(y)
element2 = browser.find_element_by_id("robotCheckbox").click()
element3 = browser.find_element_by_id("robotsRule").click()
element4 = browser.find_element_by_css_selector(".btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", element4)
element4.click()
