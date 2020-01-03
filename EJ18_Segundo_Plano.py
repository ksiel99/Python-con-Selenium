from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")

palabra_busqueda  = "sel"
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r"C:\dchrome\chromedriver.exe")
driver.get("https://google.com")
time.sleep(5)

busqueda = driver.find_element_by_name("q")
busqueda.send_keys(palabra_busqueda)
time.sleep(5)

for i in range(1,11):
	linkElement = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div/div[2]/div[2]/ul/li[" +str(i)+"]/div/div[1]/div/span/b").text
	print(palabra_busqueda + linkElement)  
driver.close()