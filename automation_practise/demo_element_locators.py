# find web elements by id and name using selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
class DemoFindElementByIdAndName():
    def find_by_id(self):
        driver=webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("https://www.abhibus.com/")
        driver.find_element(By.XPATH, '//*[@id="login-link"]/span[2]').click()
        driver.find_element(By.XPATH, '//*[@id="login-heading"]/div[2]/div[1]/div[2]/input').send_keys("7995046401")
        time.sleep(10)

elementbyid=DemoFindElementByIdAndName()
elementbyid.find_by_id()
