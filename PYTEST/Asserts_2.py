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


t=.8


@pytest.fixture(scope='module')
def setup_login():
    global driver, f

    driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
    f = Funciones_Globales(driver)
    f.Navegar("https://opensource-demo.orangehrmlive.com/", 2)
    driver.maximize_window()
    driver.implicitly_wait(20)
    f.Texto_Mixto("id", "txtUsername", "Admin", t)
    f.Texto_Mixto("id", "txtPassword", "admin123", t)
    f.Click_Mixto("id", "btnLogin", t)
    #print("entrando al sistema")

def teardown_function():
    print("fin de los test")
    driver.close()

@pytest.mark.login   #para inicializarlo. ese login se pone al aldo de -m en el comando de terminal para su test
@pytest.mark.usefixtures("setup_login")   #los usefixtures son usados para darle datos al test. para no tener que correr mismo codigo en cada test
def test_uno():
    etiqueta=f.SEX("//h1[contains(.,'Dashboard')]").text    # es igual que poner print(etiqueta.text) para que muestre ese elemento
    print(etiqueta)
    assert etiqueta=="Dashboard", "no pudiste entarr al sistema"   #si etiqueta es igual a dashboard esta bieno (,) sino "no pudiste entar al sistema"
