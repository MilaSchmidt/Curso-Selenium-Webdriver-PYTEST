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

@pytest.fixture(scope='module')
def setup_login_uno():
    global driver, f

    driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
    f = Funciones_Globales(driver)
    f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", 2)
    driver.maximize_window()
    driver.implicitly_wait(20)
    f.Texto_Mixto("id", "Email","admin@yourstore.com", t)
    f.Texto_Mixto("id", "Password","admin", t)
    f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
    print("entrando al sistema")
    yield
    print("salida del login uno")
    driver.close()

@pytest.fixture(scope='module')
def setup_login_dos():
    global driver, f

    driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
    f = Funciones_Globales(driver)
    f.Navegar("https://opensource-demo.orangehrmlive.com/", 2)
    driver.maximize_window()
    driver.implicitly_wait(20)
    f.Texto_Mixto("id", "txtUsername", "Admin", t)
    f.Texto_Mixto("id", "txtPassword", "admin123", t)
    f.Click_Mixto("id", "btnLogin", t)
    print("entrando al sistema")
    yield
    print("salida del login uno")


@pytest.mark.usefixtures("setup_login_uno")
def test_uno():
    print("entrando al sistema uno")
    f.Click_Mixto("xpath","(//p[contains(.,'Customers')])[1]",t)
    f.Click_Mixto("xpath","(//p[contains(.,'Customers')])[2]",t)
    f.Texto_Mixto("xpath","//input[contains(@id,'SearchFirstName')]","victoria",t)
    f.Click_Mixto("xpath","//button[contains(@id,'search-customers')]",2)
    f.Click_Mixto("xpath","//a[@href='/Admin/Customer/Create']",t)
    email=driver.find_element_by_xpath("//input[contains(@id,'Email')]")
    email.send_keys("juan@gmail.com"+Keys.TAB+"12345"+Keys.TAB+"juan"+Keys.TAB+"perez")
    time.sleep(3)
    f.Click_Mixto("xpath","//input[contains(@id,'Gender_Male')]",t)
    f.Texto_Mixto("xpath","//input[contains(@id,'DateOfBirth')]","8/24/1990",4)
    driver.close()




@pytest.mark.usefixtures("setup_login_dos")
def test_dos():
    print("entrando al sistema dos")
    f.Click_Mixto("xpath","//b[contains(.,'Admin')]",t)
    f.Click_Mixto("xpath","//a[contains(@id,'menu_admin_UserManagement')]",4)
    f.Texto_Mixto("xpath","//input[contains(@id,'searchSystemUser_userName')]","akshay",3)
    f.Click_Mixto("xpath","//input[contains(@id,'searchBtn')]",t)
    f.Click_Mixto("xpath","//input[contains(@id,'btnAdd')]",1)
    f.Select_Xpath_Type("//select[contains(@id,'systemUser_userType')]","index",1,3)
    driver.close()