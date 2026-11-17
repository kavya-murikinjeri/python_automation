import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class Demo_Multiple_Windows():
    def MultiWindows(self):
        driver = webdriver.Edge()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        # parent_handle= driver.current_window_handle
        # print(parent_handle)
        # import pdb; pdb.set_trace()
        parent_handle = driver.current_window_handle
        driver.find_element(By.CSS_SELECTOR, "div[title='Up to INR 2,500 OFF*'] div[class='MuiBox-root css-1nlgl51']").click()
        time.sleep(10)
        all_handles = driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                driver.execute_script("window.scrollTo(0, 0)")
                driver.find_element(By.CSS_SELECTOR,"a.simple-tab[title='Offers']").click()
                driver.find_element(By.XPATH, "//a[@href='https://www.yatra.com/offer/details/rbl-credit-card-offers']//span[@class='wfull offer-content anim']//img[@class='respnsiv-img']").click()
                time.sleep(10)
                driver.close()
                break
        driver.switch_to.window(parent_handle)



Multi = Demo_Multiple_Windows()
Multi.MultiWindows()