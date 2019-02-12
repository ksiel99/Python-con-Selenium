import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class usando_unittest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\Users\NAlvarez\Documents\explorer_driver\chromedriver.exe")

	def test_usando_implicit_wait(self):
		driver = self.driver
		driver.implicitly_wait(5) # segundos
		driver.get("http://www.google.com")	
		myDynamicElement = driver.find_element_by_name("q")
			
if __name__ == '__main__':
		unittest.main()	
