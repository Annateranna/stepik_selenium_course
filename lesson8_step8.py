from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Anna")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Anna")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("Anna@ma.ru")

    file_b = browser.find_element_by_id("file")
    # file_b.click()

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'lesson.txt')
    file_b.send_keys(file_path)

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
