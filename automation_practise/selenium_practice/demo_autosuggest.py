from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

class DemoAutoSuggest():
    def auto_suggestion(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.yatra.com/")
        # import pdb; pdb.set_trace()
        time.sleep(4)
        departure_from= driver.find_element(By.CSS_SELECTOR,"div[aria-label='Departure From New Delhi inputbox'] div[class='MuiBox-root css-70qvj9']")
        time.sleep(2)
        departure_from.click()
        time.sleep(2)
        departure=driver.find_element(By.XPATH,"//input[@id='input-with-icon-adornment']")
        departure.send_keys("New")
        time.sleep(2)
        # departure.send_keys(Keys.ENTER)
        # time.sleep(4)
        search = driver.find_elements(By.XPATH,"//div[@class='MuiBox-root css-hj42ol']/div")
        print(len(search))
        for res in search:
            if "New York" in res.text:
                res.click()
                time.sleep(4)
                break
        # if driver.find_element(By.XPATH,'//*[@id="login-heading"]/div[1]/h4'):
        #     driver.find_element(By.XPATH,'//*[@id="login-heading"]/div[1]/span/svg').click()
        # Leaving_from = driver.find_element(By.CSS_SELECTOR,"input[placeholder='Leaving From']")
        # time.sleep(4)
        # Leaving_from.click()
        # time.sleep(4)
        # Leaving_from.send_keys("New Delhi")
        # time.sleep(4)
        # Leaving_from.send_keys(Keys.ENTER)
        # time.sleep(4)
        Arrival_at= driver.find_element(By.XPATH,"//input[@id='input-with-icon-adornment']")
        time.sleep(2)
        Arrival_at.send_keys("Ma")
        time.sleep(2)
        search1=driver.find_elements(By.XPATH, "//div[@class='MuiStack-root css-wu34vq']/div")
        print(len(search1))
        time.sleep(4)
        for res1 in search1:
            if "Madurai" in res1.text:
                res1.click()
                break
        time.sleep(4)

        departure_time= driver.find_element(By.XPATH,"//div[contains(@aria-label,'Choose Thursday, September 17th, 2026')]//span[contains(@aria-label,'MAHA SHIVARATHIRI')]").click()
        time.sleep(2)
        
        #time.sleep(2)
        
    
suggest= DemoAutoSuggest()
suggest.auto_suggestion()
