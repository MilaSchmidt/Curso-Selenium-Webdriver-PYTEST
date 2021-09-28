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

t=2
class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
        self.driver.maximize_window()


    def test1(self):
        driver= self.driver
        f=Funciones_Globales(driver)
        f.Navegar("https://demoqa.com/buttons",t)
        f.Mouse_Doble("xpath","//button[contains(@id,'doubleClickBtn')]")

    '''elemento=driver.find_element_by_id("doubleClickBtn")
        
        act=ActionChains(driver) #se le pone las funciones de action chain para que oueda hacer los eventos
        # act.move_to_element(admin).click().perform() de poner solo asi es una class action de selenium y es para que hag click en ese elemento (en variable admin)
        #act.move_to_element(admin).move_to_element(sub1).move_to_element(sub2).click().perform()    #se puede concatenar varios clicks en los elementos
        act.double_click(elemento).perform()
        time.sleep(t)'''








    def tearDown(self):
            driver = self.driver
            driver.close()

if __name__ == '__main__':
        unittest.main()