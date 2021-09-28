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

t=2

def setup_function(function):
    print("esto va al inicio de cada test")  

def teardown_function(function):
    print("esto es al final de cada test")

def test_uno():
    print("test uno")

def test_dos():
    print("test dos")

def test_tres():
    print("test tres")

def test_cuatro():
    print("test cuatro")