from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.alert import Alert

class Demo_Alerts():
    def demoAlerts(self):
        driver = webdriver.Edge()
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.maximize_window()
        time.sleep(3)
        driver.switch_to.frame("iframeResult")
        driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
        time.sleep(3)
        # driver.switch_to.alert.accept()
        # time.sleep(2)

        # driver.switch_to.alert.dismiss()
        # time.sleep(2)

        # driver.switch_to.alert.send_keys("kavya")
        # driver.switch_to.alert.accept()
        # time.sleep(10)
        print(Alert(driver).text)
        time.sleep(2)

obj = Demo_Alerts()
obj.demoAlerts()