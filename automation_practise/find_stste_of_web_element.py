# how to find state of a web element
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class FindElementState():
    def element_state(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("https://www.abhibus.com/")
        # import pdb;
        # pdb.set_trace()
        driver.find_element(By.XPATH,'//*[@id="login-link"]').click()
        state= driver.find_element(By.XPATH,"//button[normalize-space()='Login']").is_enabled()
        print(state)
        time.sleep(3)
        driver.find_element(By.XPATH,"//input[@inputmode='tel']").send_keys("7995046401")
        state2= driver.find_element(By.XPATH,"//button[normalize-space()='Login']").is_enabled()
        print(state2)
        time.sleep(10)

locator = FindElementState()
locator.element_state()