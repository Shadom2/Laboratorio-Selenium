from selenium import webdriver
from selenium.webdriver.edge.service import Service

# 1. Coloca la ruta exacta donde guardaste el msedgedriver.exe
# Ejemplo: "E:/Deberes U/Análisis/Laboratorio-Selenium/msedgedriver.exe"
ruta_driver = "E:/Deberes U/Análisis/Laboratorio-Selenium/msedgedriver.exe"

# 2. Configuramos el servicio manualmente
service = Service(executable_path=ruta_driver)

# 3. Iniciamos el driver
driver = webdriver.Edge(service=service)

# 4. Navegar
driver.get("https://www.puce.edu.ec")

# Mantener el navegador abierto para tomar capturas
input("Presiona Enter para cerrar el navegador...")
