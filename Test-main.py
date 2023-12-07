import time
from selenium import webdriver
from selenium.webdriver.common.by import By
tiempo=3
d=webdriver.Chrome()
d.get("https://www.saucedemo.com/")
#maximizar pantalla
d.maximize_window()
time.sleep(7)
#Capturar imagen de salida
d.save_screenshot("Results/login.png")

# FAIL LOGIN

#Username
usr=d.find_element(By.XPATH, "//input[contains(@placeholder,'Username')]").send_keys("Lana")
time.sleep(tiempo)
#Capturar imagen de salida
d.save_screenshot("Results/IncorrectUser.png")

#Password
ps=d.find_element(By.XPATH,"//input[contains(@placeholder,'Password')]").send_keys("4569")
time.sleep(tiempo)
#Capturar imagen de salida
d.save_screenshot("Results/IncorrectPassword.png")

btn=d.find_element(By.XPATH,"//input[contains(@type,'submit')]")
btn.click()
time.sleep(tiempo)
d.refresh()


#CORRECT LOGIN
time.sleep(tiempo)
#Username
usr=d.find_element(By.XPATH, "//input[contains(@placeholder,'Username')]").send_keys("visual_user")
time.sleep(tiempo)

#Capturar imagen de salida
d.save_screenshot("Results/inser_user.png")

#Password
ps=d.find_element(By.XPATH,"//input[contains(@placeholder,'Password')]").send_keys("secret_sauce")
time.sleep(tiempo)

#Capturar imagen de salida
d.save_screenshot("Results/password.png")

btn=d.find_element(By.XPATH,"//input[contains(@type,'submit')]")
btn.click()
time.sleep(tiempo)

#Capturar imagen de salida
d.save_screenshot("Results/intro_page.png")


#Para cerrar la ventana
d.close()



