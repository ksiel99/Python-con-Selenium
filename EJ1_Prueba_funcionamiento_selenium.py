from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\NAlvarez\Documents\explorer_driver\chromedriver.exe")
driver.get("http://www.python.org")
driver.close()