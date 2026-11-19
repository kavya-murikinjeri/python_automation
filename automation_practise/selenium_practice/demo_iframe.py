from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Demo_Iframe():
    def demoIframe(self):
        driver = webdriver.Edge()
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        driver.maximize_window()
        time.sleep(3)
        driver.switch_to.frame("iframeResult")
        driver.switch_to.frame(0)
        driver.find_element(By.XPATH,"//span[@class='tnb-adventure-badge-text']").click()
        time.sleep(10)

fr = Demo_Iframe()
fr.demoIframe()