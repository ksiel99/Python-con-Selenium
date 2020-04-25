import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class usando_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"c:\dchrome\chromedriver.exe")

	def test_subir_archivo(self):
		self.driver.get("https://nicolasalvarez.com/")
		time.sleep(4)
		dobleclick = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/aside[1]/h3/span")
		actions = ActionChains(self.driver)
		actions.double_click(dobleclick).perform()
		time.sleep(3)

	def tearDown(self):
		self.driver.close()


if __name__ == '__main__':
				unittest.main()