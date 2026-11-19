from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DemoDropdown():
    def drop_down(self):
        driver = webdriver.Chrome()
        driver.get("https://www.wikipedia.org/")
        dropdown = driver.find_element(By.ID,"searchLanguage")
        dd=Select(dropdown)
        dd.select_by_index(1)
        time.sleep(3)
        dd.select_by_value("ar")
        time.sleep(3)
        dd.select_by_visible_text("Asturianu")
        


ele = DemoDropdown()
ele.drop_down()