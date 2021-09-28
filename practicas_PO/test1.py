import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from funciones.funciones import Funciones_Globales
from funciones.page_login import Pagina_Login

#en el ultimo: de la carpeta funciones, accede al archvo funciones y trae la clase ( lo que tenga dentro) funciones

tg=2

class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
        # driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")



    def test1(self):
        driver=self.driver
        f=Funciones_Globales(driver)
        f.Navegar("https://demoqa.com/text-box", tg)
        #pg=Pagina_Login(driver)
        #f.Navegar("https://www.saucedemo.com/",t)
        #f.Texto_Xpath("//input[contains(@id,'user-name')]","marta",t)
        #f.Texto_Xpath("//input[contains(@id,'password')]","admin123",t)
        #f.Texto_ID("user-name","marta",1)
        #f.Texto_ID("password","admin123",1)
        #f.Texto_Xpath_Valida("//input[contains(@id,'user-name')]","marta",t)
        #f.Texto_Xpath_Valida("//input[contains(@id,'password')]","Admin1234",t)
        #f.Texto_ID_Valida("user-name","Juan", t)
        #f.Texto_ID_Valida("password", "admin",t)
        #f.Click_Xpath_Valida("//input[contains(@id,'login-button')]",t)
        #f.Click_ID_Valida("login-button",t)
        #pg.Login_Master("https://www.saucedemo.com/","rodrigo","admin",tg)

        #f.Select_Xpath_Text("//select[contains(@id,'select-demo')]","Sunday",tg)
        #f.Select_Xpath_Type("//select[contains(@id,'select-demo')]","value","Sunday",tg)  #se puede cambiar value, text and index en la misma funcion
        #f.Select_ID_Type("select-demo","index",3,tg)
        #f.Upload_Xpath("//input[contains(@id,'fileinput')]","C://Users//Luciano//PycharmProjects//pythonProject1//imagenes//demo1.jpg",tg)
        #f.Upload_ID("fileinput","C://Users//Luciano//PycharmProjects//pythonProject1//imagenes//demo1.jpg",tg)
        #f.Check_Xpath("//input[contains(@id,'isAgeSelected')]",tg)
        #f.Check_ID("isAgeSelected",tg)
       # for n in range(2,6): #rango donde se hace el bucle, con la funcion check xpath multiples
        #    f.Check_Xpath_Multiples(2,"(//input[@type='checkbox'])["+str(n)+"]")
       # f.Texto_Mixto("id","userName","marta",tg)




#en las funciones globales se declaran cada fucnion, en page login se llaman a esas funciones y se ponen los parametros que necesita. en test se ponen los valores a esos parametros solo en 1 linea
#en FG se crean las funciones, en PL se llaman y en T1 se corre el test
    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()
