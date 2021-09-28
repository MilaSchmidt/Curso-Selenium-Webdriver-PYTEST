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


t=.5

@pytest.fixture(scope='module')   #decorador, es cmo un id para poderlo seleccionar.
def setup_login_uno():
    print("empezando el login del sistema")
    yield   #es como el teardown
    print("saliendo del sistema prueba ok")

@pytest.fixture(scope='module')
def setup_login_dos():
    print("emepzando las pruebas del sistema dos")
    yield
    print("fin de las pruebas delsistema dos")


def test_uno(setup_login_uno):      #al ponerlo de parametro le esta diciendo que cuando cora el test 1 le pase el set
    print("emepzando las pruebs del test1")

def test_dos(setup_login_dos):
    print("esto es para la prueba dos")

@pytest.mark.usefixtures("setup_login_dos")   #se usa el cod de ese fxture para esta prueba
def test_tres():
    print("prueba tres del modulo login 2")