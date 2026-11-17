from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class FindRadioButton():
    def click_radio_button(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/sql/default.asp")
        driver.find_element(By.ID,"quizoption2").click()
        en=driver.find_element(By.ID,"quizoption2").is_selected()
        print(en)
        


ele = FindRadioButton()
ele.click_radio_button()