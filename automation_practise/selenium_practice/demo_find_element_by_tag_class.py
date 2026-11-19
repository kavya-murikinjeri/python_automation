# find web elements by css selectors
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class FindElementByIdDemo():
    def locate_by_id(self):
        driver = webdriver.Chrome()
        driver.get("https://www.abhibus.com/")
        driver.find_element(By.LINK_TEXT, 'Login/SignUp').click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,'//*[@id="login-heading"]/div[2]/div[1]/div[2]/input').send_keys("7995046401")
        time.sleep(10)
        driver.find_element(By.CLASS_NAME,"btn btn-login dark filled primary md rounded-md inactive button").click()
        time.sleep(20)

locator = FindElementByIdDemo()
locator.locate_by_id()