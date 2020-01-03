from selenium  import  webdriver

driver = webdriver.Ie(executable_path=r"C:\dchrome\IEDriverServer.exe")
driver.get("http://www.google.com")
driver.close()