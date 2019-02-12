import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class usando_unittest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\Users\NAlvarez\Documents\explorer_driver\chromedriver.exe")

	def test_usando_Explicit_wait(self):
		driver = self.driver
		driver.get("http://www.google.com")	
		try:
			element = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.NAME, "q"))
	    	)
		finally:
			driver.quit()
			
if __name__ == '__main__':
		unittest.main()	


























#Explicit wait : Espera a que se ejecute ciertas condiciones para continuar corriendo el script
#Implicit wait : Espera un cierto tiempo o espera a que se carguen sientos elementos para poder seguir su proceso

#title_is
#title_contains
#presence_of_element_located
#visibility_of_element_located
#visibility_of
#presence_of_all_elements_located
#text_to_be_present_in_element
#text_to_be_present_in_element_value
#frame_to_be_available_and_switch_to_it
#invisibility_of_element_located
#element_to_be_clickable
#staleness_of
#element_to_be_selected
#element_located_to_be_selected
#element_selection_state_to_be
#element_located_selection_state_to_be
#alert_is_present