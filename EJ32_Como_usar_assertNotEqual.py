import unittest
from selenium import webdriver
import time

class usando_unittest(unittest.TestCase):

		def setUp(self):
				self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")


		def test_asserEqual(self):
				driver = self.driver
				driver.get("https://www.google.com")
				titulodelapagina = driver.title 
				time.sleep(2)
				self.assertNotEqual("Google" ,titulodelapagina, "El titulo de la pagina es igual")

		def tearDown(self):
				self.driver.close()

if __name__ == '__main__':
		unittest.main()		