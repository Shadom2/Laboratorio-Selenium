from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Ruta al chromedriver que acabas de descargar
ruta_chrome = "E:/Deberes U/Análisis/Laboratorio-Selenium/chromedriver.exe"

service = Service(executable_path=ruta_chrome)
driver = webdriver.Chrome(service=service)

driver.get("https://www.puce.edu.ec")

# Mantener el navegador abierto para tomar capturas
input("Presiona Enter para cerrar el navegador...")