# find text of an element in selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class FindElementText():
    def find_text(self):
        driver = webdriver.Chrome()
        driver.get("https://www.abhibus.com/")
        text = driver.find_element(By.XPATH,"//p[normalize-space()='Karnataka State Road Transport Corporation']").text
        print(text)
        time.sleep(10)

locator = FindElementText()
locator.find_text()