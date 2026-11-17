# how to get attribute values for a web element
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class GetAttributeValue():
    def get_value(self):
        driver = webdriver.Chrome()
        driver.get("https://www.abhibus.com/")
        value = driver.find_element(By.XPATH,"//img[@src='https://static.abhibus.com/web/flight.svg']").get_attribute("height")
        print(value)
        time.sleep(10)

locator = GetAttributeValue()
locator.get_value()