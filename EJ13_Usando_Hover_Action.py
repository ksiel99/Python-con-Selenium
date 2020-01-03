from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
driver.get("https://google.com")
time.sleep(3)
elem = driver.find_element_by_link_text("Privacidad")

hover = ActionChains(driver).move_to_element(elem)
hover.perform()