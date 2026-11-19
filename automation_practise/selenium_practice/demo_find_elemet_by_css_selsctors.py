# find web elements by id and name using selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class FindElementByIdDemo():
    def locate_by_id(self):
        driver = webdriver.Chrome()
        driver.get("https://www.abhibus.com/")
        driver.find_element(By.XPATH, '//*[@id="login-link"]').click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,'//*[@id="login-heading"]/div[2]/div[1]/div[2]/input').send_keys("7995046401")
        time.sleep(20)

locator = FindElementByIdDemo()
locator.locate_by_id()