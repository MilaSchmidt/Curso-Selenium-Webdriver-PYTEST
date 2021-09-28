import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from ..funciones.funciones import Funciones_Globales
from selenium.webdriver import ActionChains

t = 2


class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
        self.driver.maximize_window()

    def test1(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://www.saucedemo.com/", t)

        f.Texto_Mixto("xpath","//input[contains(@id,'user-name')]","Admin",3)
        f.Texto_Mixto("xpath","//input[contains(@id,'password')]","admin",3)
        f.Click_Mixto("xpath","//input[contains(@id,'login-button')]",2)








    def tearDown(self):
        driver = self.driver
        driver.close()


if __name__ == '__main__':
    unittest.main()