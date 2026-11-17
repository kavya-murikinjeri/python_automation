import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class DemoJsExecution():
    def js_execution(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.execute_script("window.open('https://www.abhibus.com/','_self');")
        time.sleep(4)
        demo_element = driver.execute_script("return document.getElementsByTagName('img')[6];")
        driver.execute_script("arguments[0].click();", demo_element)
        time.sleep(5)
        
        

locator = DemoJsExecution()
locator.js_execution()