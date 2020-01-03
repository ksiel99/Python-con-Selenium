from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time

palabra_busqueda = "sele"
driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
driver.get("https://www.google.com")
time.sleep(5)

busqueda = driver.find_element_by_name("q")
busqueda.send_keys(palabra_busqueda)
time.sleep(5)

for i in range(1,11):
	elementos = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div/div[2]/div[2]/ul/li["+str(i)+"]/div/div[1]/div/span/b").text
	print(palabra_busqueda + elementos)
driver.close()
