from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x1 = int(x_element.text)
    y_element = browser.find_element_by_id("num2")
    y1 = int(y_element.text)
    total = x1 + y1

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(total))
    # browser.find_element_by_tag_name("select").click()
    # browser.find_element_by_css_selector("[value=total]").click()

    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
