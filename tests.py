
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get()  # ex http//

driver.quit()

