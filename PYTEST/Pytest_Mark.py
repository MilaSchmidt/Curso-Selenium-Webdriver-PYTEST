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

@pytest.mark.run
def test_uno():
    print("test uno")

@pytest.mark.notrun
def test_dos():
    print("test dos")

@pytest.mark.notrun
def test_tres():
    print("test tres")

@pytest.mark.run
def test_cuatro():
    print("test cuatro")

@pytest.mark.run
def test_cinco():
    print("test cinco")

@pytest.mark.notrun    #con los marcadores en la terminal puedo hacer elcomando -m para indicar que  hay uno y ponerle su nombre al lddo
def test_seis():
    print("test seis")

    #con el comando -m "not..." indico que quiero correr todos los marcadors menos(not)

    #en lgar de poner nombre se puede poner run-not run y en el comando poner -m run para que corran los validados asi.
    #si pongo skip por mas que tenga o no un run el no va a correr