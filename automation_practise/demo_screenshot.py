import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class DemoScreenshot():
    def take_screenshot(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        
        
        driver.get("https://www.yatra.com/")
        # import pdb; pdb.set_trace()
        time.sleep(2)
        driver.find_element(By.XPATH,"//div[normalize-space()='Login / Signup']").click()
        time.sleep(2)
        login_button = driver.find_element(By.XPATH,"//button[normalize-space()='Login']")
        login_button.screenshot(".\\test.png")
        time.sleep(2)
        login_button.click()
        time.sleep(2)
        driver.get_screenshot_as_file(".\\error.png")
        driver.save_screenshot(".\\test1.png")
        time.sleep(4)
        

Screen = DemoScreenshot()
Screen.take_screenshot()