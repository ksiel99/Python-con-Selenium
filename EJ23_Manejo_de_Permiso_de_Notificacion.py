from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

opciones = Options()

#enviar argumentos(1 permitiendo la notificacion,  2 bloquean la notificacion)
opciones.add_experimental_option("prefs",{
	"profile.default_content_setting_values.notifications" : 1		
	})

driver = webdriver.Chrome(chrome_options=opciones, executable_path='C:\dchrome\chromedriver.exe')
driver.get('https://developer.mozilla.org/es/docs/Web/API/notification')
time.sleep(3)
