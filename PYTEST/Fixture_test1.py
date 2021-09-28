import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from funciones import Funciones_Globales
from Page_Login import Funciones_Login
from selenium.webdriver import ActionChains


driver=""  #que quede en cero
f=""
t=.5
def setup_function(function):
    global driver,f   #para poder usarla en todos aldos. dos variables globales
    driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
    driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    driver.maximize_window()
    f = Funciones_Globales(driver)
    f.Texto_Mixto("id", "Email", "admin@yourstore.com", t)
    f.Texto_Mixto("id", "Password", "admin", t)
    f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)

    print("iniciando nuestros tests")

def teardown_function(function):
    print("fin de los tests")
    driver.close()

def test_uno():

    f.Click_Mixto("xpath", "//a[@href='#'][contains(.,'Catalog')]", t)
    f.Click_Mixto("xpath", "(//p[contains(.,'Products')])[1]", t)
    f.Texto_Mixto("xpath", "//input[contains(@id,'SearchProductName')]", "computer", t)
    f.Click_Mixto("xpath", "//button[contains(@id,'search-products')]", t)

def test_dos():
    #driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
    f=Funciones_Globales(driver)
    f.Click_Mixto("xpath", "//a[@href='#'][contains(.,'Catalog')]", t)
    f.Click_Mixto("xpath", "(//p[contains(.,'Products')])[1]", t)
    f.Click_Mixto("xpath","//a[@href='/Admin/Product/Create']",t)
    f.Texto_Mixto("xpath","//input[@id='Name']","laptop dell",t)
    f.Texto_Mixto("xpath","//textarea[contains(@id,'ShortDescription')]","laptop modelo nuevo tipo dell",t)
    f.Click_Mixto("xpath","//span[@class='tox-mbtn__select-label'][contains(.,'File')]",t)
    f.Click_Mixto("xpath","//div[@class='tox-collection__item-label'][contains(.,'New document')]",t)
    driver.switch_to.frame(0)   #como ele elemento estaba dentro de un iframe, le dice al driver que se cambie a frame con index 0
    #f.Texto_Mixto("id","tinymce","descripcion larga",t)
    campo=driver.find_element_by_id("tinymce")
    campo.send_keys("descripcion larga"+Keys.TAB+"3434")
    time.sleep(3)



