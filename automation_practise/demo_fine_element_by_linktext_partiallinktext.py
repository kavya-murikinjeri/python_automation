# find web elements by css selectors
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class FindElementByIdDemo():
    def locate_by_id(self):
        driver = webdriver.Chrome()
        driver.get("https://www.abhibus.com/")
        #driver.find_element(By.LINK_TEXT, 'Login/SignUp').click()
        driver.find_element(By.PARTIAL_LINK_TEXT,"Login").click()
        
        time.sleep(20)

locator = FindElementByIdDemo()
locator.locate_by_id()