from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Multiple_Windows():
    def multiple_windows_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/hotels")
        driver.maximize_window()
        time.sleep(4)
        driver.find_element(By.XPATH,"//p[normalize-space()='SME/Corporates']").click()
        parent = driver.current_window_handle
        print(parent)
        driver.find_element(By.XPATH,"//span[normalize-space()='Book & Manage your Business Travel']").click()
        time.sleep(2)
        # all_handles=driver.window_handles
        # print(all_handles)
        # for handle in all_handles:
        #     if handle != parent:
        #         driver.switch_to.window(handle)
        #         driver.find_element(By.XPATH,"//img[@alt='Play Store']").click()
        #         driver.close()
        #         time.sleep(4)
        #         break
        # time.sleep(3)
        # driver.switch_to.window(parent)
       





Multi=Multiple_Windows()
Multi.multiple_windows_demo()