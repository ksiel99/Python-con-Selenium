import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
driver.get("file:///C:/Users/alber/Desktop/ciclar%20informacion/login.html")
time.sleep(3)

#inicia ciclo de auto llenado de form
with open('datos.txt') as file:
	 for i, line in enumerate(file):
	 		usuario = (line)
	 		sep = ","
	 		dividir = usuario.split(sep)
	 		try:
	 			gotdata = dividir[1]
	 			user = dividir[0]
	 			pas = dividir[1]
	 		except IndexError:
	 			gotdata = 'null'
	 		
	 		print(user)
	 		print(pas)
	 		driver.find_element_by_id("login").send_keys(user)
	 		time.sleep(3)
	 		driver.find_element_by_id("cont").send_keys(pas)
	 		time.sleep(3)
	 		driver.find_element_by_xpath("/html/body/p[2]/input[2]").click()
	 		time.sleep(3)

file.close()
driver.close()