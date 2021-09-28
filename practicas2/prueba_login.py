import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException


class PruebaLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
        # driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
        t = 2

    def test_login1(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        nom = driver.find_element_by_xpath("//input[contains(@id,'user-name')]")
        clave = driver.find_element_by_xpath("//input[contains(@id,'password')]")
        bt = driver.find_element_by_xpath("//input[contains(@id,'login-button')]")
        nom.send_keys("rodrigo")
        clave.send_keys("admin123")
        bt.click()
        error = driver.find_element_by_xpath("//h3[contains(@data-test,'error')]")
        error = error.text
        # print(error)
        if (error == "Epic sadface: Username and password do not match any user in this service"):
            print("El error de los datos es correcto")
            print("Prueba uno Ok")
        time.sleep(3)

    def test_login2(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        nom = driver.find_element_by_xpath("//input[contains(@id,'user-name')]")
        clave = driver.find_element_by_xpath("//input[contains(@id,'password')]")
        bt = driver.find_element_by_xpath("//input[contains(@id,'login-button')]")
        nom.send_keys("")
        clave.send_keys("admin123")
        bt.click()
        error = driver.find_element_by_xpath("//h3[contains(@data-test,'error')]")
        error = error.text
        print(error)

        if (error == "Epic sadface: Username is required"):
            print("Falta el nombre")
            print("Prueba dos Ok")

        time.sleep(3)



    def test_login3(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        nom = driver.find_element_by_xpath("//input[contains(@id,'user-name')]")
        clave = driver.find_element_by_xpath("//input[contains(@id,'password')]")
        bt = driver.find_element_by_xpath("//input[contains(@id,'login-button')]")
        nom.send_keys("marta")
        clave.send_keys("")
        bt.click()
        error = driver.find_element_by_xpath("//h3[contains(@data-test,'error')]")
        error = error.text
        print(error)

        if (error == "Epic sadface: Password is required"):
            print("Falta contraseña")
            print("Prueba tres Ok")

        time.sleep(3)

    def test_login4(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        nom = driver.find_element_by_xpath("//input[contains(@id,'user-name')]")
        clave = driver.find_element_by_xpath("//input[contains(@id,'password')]")
        bt = driver.find_element_by_xpath("//input[contains(@id,'login-button')]")
        nom.send_keys("")
        clave.send_keys("")
        bt.click()
        error = driver.find_element_by_xpath("//h3[contains(@data-test,'error')]")
        error = error.text
        print(error)

        if (error == "Epic sadface: Username is required"):
            print("Faltan dos campos")
            print("Prueba cuatro pendiente")  #fata mensaje para cuando ambos campos no se completan

        time.sleep(3)

    def test_login5(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        nom = driver.find_element_by_xpath("//input[contains(@id,'user-name')]")
        clave = driver.find_element_by_xpath("//input[contains(@id,'password')]")
        bt = driver.find_element_by_xpath("//input[contains(@id,'login-button')]")
        nom.send_keys("standard_user")
        clave.send_keys("secret_sauce")
        bt.click()
        time.sleep(3)


        elemento = driver.find_element_by_xpath("//div[contains(@class,'app_logo')]")
        elemento.is_enabled()
        print("el elemento es: " +str(elemento))
        time.sleep(1)

    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()






























