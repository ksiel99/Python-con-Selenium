from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
driver.get("https://www.w3schools.com/html/html_tables.asp")
time.sleep(5)

valor = driver.find_element_by_xpath("//*[@id='customers']/tbody/tr[2]/td[2]").text
print(valor)

rows=len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr")) 
cols=len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[1]/th")) 

print(rows)
print(cols)

for n in range(2,rows+1):
	for b in range(1,cols+1):
		dato=driver.find_element_by_xpath("//*[@id='customers']/tbody/tr["+str(n)+"]/td["+str(b)+"]").text
		print(dato, end='							')
	print()
