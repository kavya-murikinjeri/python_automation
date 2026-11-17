# find web elements by css selectors
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class FindElementByIdDemo():
    def locate_by_id(self):
        driver = webdriver.Chrome()
        driver.get("https://www.abhibus.com/")
        lis=driver.find_elements(By.TAG_NAME,"a")
        print(len(lis))
        for name in lis:
            print(name.text)
        time.sleep(20)

locator = FindElementByIdDemo()
locator.locate_by_id()