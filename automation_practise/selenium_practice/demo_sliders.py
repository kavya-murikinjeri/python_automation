from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

class Demo_Slider():
    def demoSliders(self):
        driver = webdriver.Edge()
        driver.get("https://www.snapdeal.com/products/women-apparel-sarees")
        driver.maximize_window()
        time.sleep(3)
        # import pdb; pdb.set_trace()
        achains=ActionChains(driver)
        ele1=driver.find_element(By.XPATH,"//a[@class='price-slider-scroll left-handle ui-slider-handle ui-state-default ui-corner-all hashAdded']")
        ele2=driver.find_element(By.XPATH,"//a[@class='price-slider-scroll right-handle ui-slider-handle ui-state-default ui-corner-all hashAdded']")
        # achains.drag_and_drop_by_offset(ele1,40,0).perform()
        achains.click_and_hold(ele1).pause(1).move_by_offset(40,0).release().perform()
        time.sleep(15)

sl=Demo_Slider()
sl.demoSliders()