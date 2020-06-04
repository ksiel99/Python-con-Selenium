import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time



class usando_unittest(unittest.TestCase):

	def setUp(self):
		chromeOptions=Options() 
		chromeOptions.add_experimental_option("prefs", {
   	    "download.default_directory" : "C:\\dchrome",
        })
		self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe",chrome_options=chromeOptions)

	def test_usando_toggle(self):
		driver = self.driver
		driver.get("https://www.w3schools.com/howto/tryit.asp?filename=tryhow_html_download_link")
		time.sleep(3)
		driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[7]/div[4]/div/div/iframe"))
		time.sleep(3)
		driver.find_element_by_xpath("/html/body/p[2]/a").click()
		time.sleep(5)
		
	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()