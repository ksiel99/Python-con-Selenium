from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
 
driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
driver.get("https://www.w3schools.com/") 
time.sleep(5)
continue_link = driver.find_element_by_link_text('Learn PHP')
#continue_link = driver.find_element_by_partial_link_text('Lear')
continue_link.click()