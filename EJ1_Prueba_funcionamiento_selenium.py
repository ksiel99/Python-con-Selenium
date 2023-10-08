from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(r"E:\drivers\chromedrvier\chromedriver.exe")
driver = webdriver.Chrome(service = s)
driver.get("http://www.python.org")
#driver.close()
