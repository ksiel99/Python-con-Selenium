from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
driver.get("https://www.google.com")
time.sleep(3)
displaelemen = driver.find_element_by_name("btnI")
print(displaelemen.is_displayed())# regresa true o false si ya cargo el elemento
print(displaelemen.is_enabled())# regresa un true o false si el elemento esta disponible

