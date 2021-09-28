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


@pytest.mark.validarif
def test_validar_if():
    nom1="rodrigo"
    nom2="Rodrigo"

    assert nom1==nom2, "los nombres no son iguales"
    '''
     assert nom1==nom2, "los nombres no son iguales"
E       AssertionError: los nombres no son iguales
E       assert 'rodrigo' == 'Rodrigo'
E         - Rodrigo
E         ? ^
E         + rodrigo
E         ? ^
   nos pone en que letra esta la diferencia que tira el error
    
    '''


    '''
    a=21
    b=20
    
    assert a<b, "a es menos que b"
    
    en el test te marca
    assertionError
    assert 21<20
    
    a=19
    b=23
    c=18
    
    assert a<=b and a<=c, "a no es menor o igual que b o a no es menor o igual que c"
    error
    assert (19<=23 and 19<=18)
    
    
   @pytest.mark.validarif 
   def test_validar_if():
   dato="Ram"
   frase="dentro de las computadoras hay meoria ram 
  
    assert dato in frase , "el dato no esta dentro de la fras"
    si el dato esta dentro no dice nada, sino va a decir lo que tiene dentro de comillas
      no va a pasar el test porque va palabra por palabra buscando el dato dentro de frase. solo cuando este ogual va apasr.
    
    doble validacion
    @pytest.mark.validarif 
   def test_validar_if():
   a=20
   b=25
   if (a==b):
     print ("los datos no son iguales")
     assert a==b
   else:
    assert a==b, "no son iguales"
    
    El assert es una instruccion de Python que te permite definir condiciones que deban cumplirse siempre
    En caso que la expresion booleana sea True assert no hace nada y en caso de False dispara una excepcion
    '''