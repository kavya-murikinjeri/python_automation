from selenium import webdriver
import selenium
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Firefox()
# driver = webdriver.Chrome()
#driver = webdriver.Edge()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com/")
driver.maximize_window()
print(driver.title)
time.sleep(10)