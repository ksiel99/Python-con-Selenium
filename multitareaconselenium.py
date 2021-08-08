import time
from selenium import webdriver 
from threading import Thread, Barrier

def func(threads):

	driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
	driver.get(url)

	driver.find_element_by_id("email").send_keys("tu_corre")
	driver.find_element_by_id("pass").send_keys("tu_contraseña")
	ingresar = driver.find_element_by_name("login")

	threads.wait()
	ingresar.click()

url='https://www.facebook.com/'

numero_multitareas = 6

barrier = Barrier(numero_multitareas)

threads = []

for _ in range(numero_multitareas):
	i = Thread(target=func, args=(barrier,))
	i.start()
	threads.append(i)

for i in threads:
	i.join()