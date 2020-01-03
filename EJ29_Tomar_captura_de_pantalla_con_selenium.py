from selenium import webdriver
driver =webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
driver.get("https://www.youtube.com/channel/UCcT6IFddIod7xURc7a7q3Bg?view_as=subscriber")
driver.get_screenshot_as_file("C:\\Users\\alber\\Documents\\Cursos programacion canal ksiel99\\Python con selenium ejercicios\\mi_canal.png")