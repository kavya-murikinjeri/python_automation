from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

class Demo_Alerts():
    def demoAlerts(self):
        driver = webdriver.Edge()
        # driver.get("https://www.yatra.com/")
        # driver.maximize_window()
        # time.sleep(10)
        # # import pdb; pdb.set_trace()
        ac=ActionChains(driver)
        # ele=driver.find_element(By.XPATH,"//div[normalize-space()='Login / Signup']")
        # ac.move_to_element(ele).click().perform()
        # time.sleep(2)

        driver.get("https://requestly.com/blog/mouse-hover-in-selenium/")
        driver.maximize_window()
        time.sleep(2)
        ac.move_to_element(driver.find_element(By.XPATH,"//button[normalize-space()='Resources']")).perform()
        time.sleep(3)
        driver.find_element(By.XPATH,"//div[@id='mm-resources']//a[normalize-space()='Blog']").click()
        time.sleep(4)


        


act=Demo_Alerts()
act.demoAlerts()