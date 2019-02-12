import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class usando_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\Users\NAlvarez\Documents\explorer_driver\chromedriver.exe")

	def test_usando_toggle(self):
		driver = self.driver
		driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
		time.sleep(3)
		radio_bt = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/input[4]")
		radio_bt.click()
		time.sleep(3)
		radio_bt.click()
		time.sleep(3)

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()