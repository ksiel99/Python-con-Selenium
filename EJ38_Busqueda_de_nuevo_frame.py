import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class usando_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

	def test_buscar_frame(self):
		driver = self.driver
		driver.get("http://www.google.com")
		time.sleep(3)
		click1 = driver.find_element_by_id("gbwa")
		time.sleep(3)
		click1.click()
		time.sleep(2)
		driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div[3]/iframe"))
		time.sleep(3)
		click2 = driver.find_element_by_id("yDmH0d")
		time.sleep(2)
		click2.click()
		time.sleep(5)

if __name__ == '__main__':
	unittest.main()


