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


def get_Data():
    return [
        ("rodrigo","1234"),
        ("juan", "144234"),
        ("pedro", "1fr234"),
        ("erica", "1233fs4"),
        ("Admin", "admin123")

    ]

@pytest.mark.login
@pytest.mark.parametrize("user,clave",get_Data())  #con esto le decimos, vas a pasar user y clave de la lista get data
def test_login(user,clave):
    global driver, f

    driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
    f = Funciones_Globales(driver)
    f.Navegar("https://opensource-demo.orangehrmlive.com/", 2)
    driver.maximize_window()
    driver.implicitly_wait(20)
    f.Texto_Mixto("id", "txtUsername",user, t)
    f.Texto_Mixto("id", "txtPassword", clave, t)
    f.Click_Mixto("id", "btnLogin", t)
    print("entrando al sistema")

def teardown_function():
    print("salida del test")
    driver.close()
