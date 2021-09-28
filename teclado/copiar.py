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
        f.Navegar("https://demoqa.com/automation-practice-form", t)
        f.Texto_Mixto("xpath","//input[contains(@id,'firstName')]","juan",1)

        act=ActionChains(driver)
        act.key_down(Keys.CONTROL).send_keys('a').key_up((Keys.CONTROL)).perform()   #key down es oprimir-->tecla control (keys.control). send keys 'a' lo que hace es seleccionarlo. key up(keys.control) lo levanta cn up
        time.sleep(2)
        act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
        act.send_keys(Keys.TAB)
        act.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        time.sleep(2)
#con el key down dice que mantenga presionado la tecl ctrl, el send keys que escriba a y luego levante y ejecute. (hace un ctrl+alt para seleccionar)
    #despues dice presionar crtl y escribir c para copiar. luego dice que escriba tab para irse al costado y haga ctrl v para pegar




    def tearDown(self):
        driver = self.driver
        driver.close()


if __name__ == '__main__':
    unittest.main()