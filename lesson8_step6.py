from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x1 = x_element.text
    y = calc(x1)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    check_b = browser.find_element_by_id("robotCheckbox")
    check_b.click()

    radio_b = browser.find_element_by_id("robotsRule")
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);", radio_b)
    radio_b.click()

    button = browser.find_element_by_css_selector("[type='submit']")
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
