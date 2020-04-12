from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
 
driver = webdriver.Chrome(executable_path=r"C:\Users\NAlvarez\Documents\explorer_driver\chromedriver.exe")
driver.get("https://gmail.com") 
time.sleep(5)

usuario = driver.find_element_by_id("identifierId")
usuario.send_keys("tucorreo")
usuario.send_keys(Keys.ENTER)
time.sleep(3)
acceso = driver.find_element_by_name("password")
acceso.send_keys("tuconstraseña")
acceso.send_keys(Keys.ENTER)
