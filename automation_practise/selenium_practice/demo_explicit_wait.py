from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DemoExplicitWait():
    def demoExpWait(self):
        driver=webdriver.Chrome()
        driver.get("https://www.abhibus.com/")
        driver.maximize_window()
        # Implicit wait
        # driver.implicitly_wait(10)
        # import pdb; pdb.set_trace()
        # # driver.find_element(By.XPATH,"//a[@id='login-link']").click()
        # driver.find_element(By.CSS_SELECTOR,"input[type='text'][inputmode='tel']").send_keys("7995046401")

        # Explicit wait
        wait=WebDriverWait(driver,30)
        mobile= wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input[type='text'][inputmode='tel']")))

        driver.find_element(By.CSS_SELECTOR,"input[type='text'][inputmode='tel']").send_keys("7995046401")
        

exp=DemoExplicitWait()
exp.demoExpWait()