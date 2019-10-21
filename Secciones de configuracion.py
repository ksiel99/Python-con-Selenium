import configparser
configuracion = configparser.ConfigParser()

configuracion['General'] = {'chrome' : 'C:\dchrome\chromedriver.exe'}
configuracion['Paginas'] = {'google' : 'https://www.google.com'}

with open('config.cfg', 'w') as archivoconfig:
    configuracion.write(archivoconfig)