from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DemoFluentWait():
    def demoFluWait(self):
        driver=webdriver.Chrome()
        driver.get("https://www.abhibus.com/")
        driver.maximize_window()
        wait=WebDriverWait(driver,20,2)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input[type='text'][inputmode='tel']"))).send_keys("7995046401")

flu=DemoFluentWait()
flu.demoFluWait()