from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class FindHiddenElement():
    def hidden_element(self):
        driver = webdriver.Chrome()
        # driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        # state= driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
        # print(state)
        # driver.find_element(By.XPATH,"//button[normalize-space()='Toggle Hide and Show']").click()
        # state1= driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
        # print(state1)
        driver.get("https://www.abhibus.com/")
        driver.find_element(By.XPATH,"//span[normalize-space()='Hotels']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@placeholder='Rooms & Guests']").click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,"//*[@data-testid='counter-increment-children']").click()
        state= driver.find_element(By.XPATH,"//select[@id='child-age']").is_displayed()
        print(state)
        time.sleep(3)
        driver.find_element(By.XPATH,"//*[@data-testid='counter-decrement-children']").click()
        
        state1= driver.find_element(By.XPATH,"//select[@id='child-age']").is_displayed()
        print(state1)


ele = FindHiddenElement()
ele.hidden_element()