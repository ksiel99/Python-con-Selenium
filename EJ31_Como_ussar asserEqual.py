import unittest
from selenium import webdriver
import time
class usando_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

	def test_assertEqual(self):
		driver = self.driver
		driver.get("http://www.google.com")
		titulodepagina = driver.title 	
		self.assertEqual("Google123", titulodepagina,"El titulo de la pagina es incorrecto")

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()
