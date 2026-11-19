from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

class Demo_Context_Double_Click():
    def demoClicks(self):
        driver = webdriver.Edge()
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        time.sleep(3)
        achains=ActionChains(driver)
        # context - click(right click)
        # aelement=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
        # achains.context_click(aelement).perform()

        time.sleep(5)

        #double click
        aelement=driver.find_element(By.XPATH,"//button[normalize-space()='Double-Click Me To See Alert']")
        achains.double_click(aelement).perform()
        time.sleep(5)

ob=Demo_Context_Double_Click()
ob.demoClicks()


    
