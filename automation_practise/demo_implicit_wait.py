from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

class Demo_Implicit_Wait():
    def demoImplicitWait(self):
        driver = webdriver.Edge()
        driver.implicitly_wait(10)
        driver.get("https://login.salesforce.com/")
        driver.maximize_window()
        driver.find_element(By.XPATH,"//input[@id='username']").send_keys("Kavya")

im=Demo_Implicit_Wait()
im.demoImplicitWait()