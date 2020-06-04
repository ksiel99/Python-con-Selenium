import unittest
from selenium import webdriver
import time

class usando_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

	def test_usando_toggle(self):
		driver = self.driver
		driver.get("https://www.w3schools.com/howto/howto_html_file_upload_button.asp")
		time.sleep(3)
		driver.find_element_by_id("myFile").send_keys("c:\\Users\\alber\\Pictures\\modelo s tesla.jpg")
		time.sleep(5)
		
	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()