from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

class Demo_Drag_And_Drop():
    def demoDragAndDrop(self):
        driver = webdriver.Edge()
        driver.get("https://www.tutorialspoint.com/selenium/practice/droppable.php")
        driver.maximize_window()
        time.sleep(3)
        achains=ActionChains(driver)
        ele1=driver.find_element(By.XPATH,"//div[@id='draggable']")
        # ele2=driver.find_element(By.XPATH,"//div[@id='droppable']")
        # achains.drag_and_drop(ele1,ele2).perform()
        achains.drag_and_drop_by_offset(ele1, 697,341).perform()
        time.sleep(5)

dd=Demo_Drag_And_Drop()
dd.demoDragAndDrop()
