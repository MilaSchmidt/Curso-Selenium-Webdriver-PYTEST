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
def test_login_uno():
    driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
    fl=Funciones_Login(driver)   #fl es la class funcion login que se tiene que importar desde page login funciones login.
    fl.L1("rodrigo@gmail.com","1234","No customer account found")
    fl.L2("rodrigo","2323","Wrong email")
    fl.L3("admin@yourstore.com","admin","Dashboard")











