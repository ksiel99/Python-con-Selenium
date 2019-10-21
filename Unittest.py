import unittest
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class usando_unittest(unittest.TestCase):

	def setUp(self):
		configuracion = configparser.ConfigParser()
		configuracion.read('config.ini')
		configuracion.sections()
		gexplorer = configuracion['General']['chrome']
		self.page = configuracion['Paginas']['google']
		self.driver = webdriver.Chrome(executable_path=gexplorer)


	def test_usando_implicit_wait(self):
		driver = self.driver
		driver.implicitly_wait(5) # segundos
		driver.get(self.page)	
		myDynamicElement = driver.find_element_by_name("q")
			
if __name__ == '__main__':
		unittest.main()	