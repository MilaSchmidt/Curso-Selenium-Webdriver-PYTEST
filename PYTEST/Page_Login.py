import time


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from funciones import Funciones_Globales

class Funciones_Login():

    def __init__(self,driver):    #para cuando queremos inicializar una class de funciones. 
        self.driver=driver

    def L1(self,email,clave,message,t=.1):

        driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
        f = Funciones_Globales(driver)
        f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", 2)
        driver.maximize_window()
        f.Texto_Mixto("id", "Email", email, t)
        f.Texto_Mixto("id", "Password", clave, t)
        f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
        e1 = f.SEX("//li[contains(.,'No customer account found')]")  # error 1 es igual a la funcion que encuentre ese valor (xpath) y lo devuelva
        e1 = e1.text  # se extrae el texto de ese elemento localizado. e1= e1 en su texto
        print(e1)  #imprima ese error
        if (e1 == message):
            print("el error es correcto")
        else:
            print("no esta bien el error")
        driver.close()


    def L2(self,email,clave,message,t=.1):

        driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
        f = Funciones_Globales(driver)
        f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", 2)
        driver.maximize_window()
        f.Texto_Mixto("id", "Email", email, t)
        f.Texto_Mixto("id", "Password",clave, t)
        f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
        e1 = f.SEX("//span[contains(@id,'Email-error')]")  # error 1 es igual a la funcion que encuentre ese valor (xpath) y lo devuelva
        e1 = e1.text
        print(e1)

        if (e1 == message):
            print("Email no valido prueba exitosa")
        else:
            print("prueba de Email no exitoso")
        driver.close()

    def L3(self,email,clave,message,t=.1):
        driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
        f = Funciones_Globales(driver)
        f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", 2)
        driver.maximize_window()
        f.Texto_Mixto("id", "Email", email, t)
        f.Texto_Mixto("id", "Password",clave, t)
        f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
        e1 = f.SEX(
            "//h1[contains(.,'Dashboard')]")  # error 1 es igual a la funcion que encuentre ese valor (xpath) y lo devuelva. lo valide
        e1 = e1.text
        print(e1)  # imprime el valor que pide que busque x xptah

        if (e1 ==message):
            print("Login exitoso")  # imprime eso si aparece el error1 de la pagina
        else:
            print("prueba no exitosa")
        driver.close()
