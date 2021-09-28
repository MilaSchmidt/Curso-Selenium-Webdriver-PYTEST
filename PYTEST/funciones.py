import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

class Funciones_Globales():

    def __init__(self,driver):
        self.driver=driver

    def Tiempo(self,tie):
        t=time.sleep(tie)
        return t

    def Navegar(self, Url,Tiempo):
        self.driver.get(Url)
        self.driver.maximize_window()
        print("Página abierta: "+str(Url))
        t = time.sleep(Tiempo)
        return t

    def Texto_Mixto(self,tipo,selector,texto,tiempo):
        if(tipo=="xpath"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element_by_xpath(selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto -> {} ".format(selector,texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif(tipo == "id"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element_by_id(selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto -> {} ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t

    def Click_Mixto(self, tipo, selector,tiempo):
        if (tipo == "xpath"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element_by_xpath(selector)
                val.click()
                print("dando click en {} -> {} ".format(selector, selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element_by_id(selector)
                val.click()
                print("dando click en {} -> {} ".format(selector, selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t


    def Salida(self):
        print("Se termina la prueba Exitosamente")



    def Select_Xpath_Type(self, xpath,tipo,dato, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element_by_xpath(xpath)
            val=Select(val)
            if(tipo=="text"):
                val.select_by_visible_text(dato)
            elif(tipo=="index"):
                val.select_by_index(dato)
            elif(tipo=="value"):
                val.select_by_value(dato)
            print("El campo Seleccionado es {} ".format(dato))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento" + xpath)
            return t

    def Select_ID_Type(self, id, tipo, dato, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element_by_id(id)
            val = Select(val)
            if (tipo == "text"):
                val.select_by_visible_text(dato)
            elif (tipo == "index"):
                val.select_by_index(dato)
            elif (tipo == "value"):
                val.select_by_value(dato)
            print("El campo Seleccionado es {} ".format(dato))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento" + id)
            return t

    def Upload_Xpath(self, xpath,ruta,tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element_by_xpath(xpath)
            val.send_keys(ruta)
            print("Se carga la imagen {} ".format(ruta))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento" + xpath)
            return t

    def Upload_ID(self, id,ruta,tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element_by_id(id)
            val.send_keys(ruta)
            print("Se carga la imagen {} ".format(ruta))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento" + id)
            return t

    #Funciòn Radio y Check
    def Check_Xpath(self, xpath, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element_by_xpath(xpath)
            val.click()
            print("Click en el elemento {} ".format(xpath))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento" + xpath)
            return t



    def Check_ID(self, id, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element_by_id(id)
            val.click()
            print("Click en el elemento {} ".format(id))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento" + id)
            return t

    def Check_Xpath_Multiples(self, tiempo, *args):
        try:
            for num in args:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, num)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element_by_xpath(num)
                val.click()
                print("Click en el elemento {} ".format(num))
                t = time.sleep(tiempo)
                return t
        except TimeoutException as ex:
            for num in args:
                print(ex.msg)
                print("No se encontro el Elemento" + num)

    def Existe(self, tipo, selector, tiempo):
        if (tipo == "xpath"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element_by_xpath(selector)
                print("El elemento  {} -> existe ".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return "No Existe"
        elif (tipo == "id"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element_by_id(selector)
                print("El elemento  {} -> existe ".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return "No Existe"

    def Mouse_Doble (self,tipo,selector,tiempo=.2):
        if(tipo=="xpath"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element_by_xpath(selector)
                act=ActionChains(self.driver)
                act.double_click(val).perform()
                print("doble click en {}".format(selector))
                t=time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("no se encuentra"+selector)
                return t
        if(tipo=="id"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element_by_id(selector)
                act= ActionChains(self.driver)
                act.double_click(val).perform()
                print("doble click en {}".format(selector))
                t=time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("no se encuentra"+selector)
                return t


    def Mouse_Derecho (self,tipo,selector,tiempo=.2):
        if(tipo=="xpath"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element_by_xpath(selector)
                act=ActionChains(self.driver)
                act.context_click(val).perform()
                print("click derecho en {}".format(selector))
                t=time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("no se encuentra"+selector)
                return t
        if(tipo=="id"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element_by_id(selector)
                act= ActionChains(self.driver)
                act.context_click(val).perform()
                print(" click derecho en {}".format(selector))
                t=time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("no se encuentra"+selector)
                return t

    def SEX(self, elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element_by_xpath(elemento)
        return val

    def SEI(self, elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element_by_id(elemento)
        return val





    def Mouse_DragDrop (self,tipo,selector,destino,tiempo=.2):
        if(tipo=="xpath"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element_by_xpath(selector)
                val2=self.SEX(destino)
                act=ActionChains(self.driver)
                act.drag_and_drop(val,val2).perform()
                print("se solto el elemento {}".format(selector))
                t=time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("no se encuentra"+selector)
                return t
        if(tipo=="id"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element_by_id(selector)
                val2=self.SEI(destino)
                act= ActionChains(self.driver)
                act.drag_and_drop(val,val2).perform()
                print("se solto el elemento {}".format(selector))
                t=time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("no se encuentra"+selector)
                return t

    def Mouse_DragDropXY (self,tipo,selector,x,y,tiempo=.2):
        if(tipo=="xpath"):
            try:
                self.driver.switch_to.frame(0)
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element_by_xpath(selector)

                act=ActionChains(self.driver)
                act.drag_and_drop_by_offset(val,x,y).perform()
                print("se solto el elemento {}".format(selector))
                t=time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("no se encuentra"+selector)
                return t
        if(tipo=="id"):
            try:

                self.driver.switch_to.frame(0)   #con esto le digo que se vaya a esa ventana del iframe. el 0 es el primero que encuentre.
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element_by_id(selector)

                act= ActionChains(self.driver)
                act.drag_and_drop_by_offset(val, x, y).perform()
                print("se solto el elemento {}".format(selector))
                t=time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("no se encuentra"+selector)
                return t

    def ClickXY (self,tipo,selector,x,y,tiempo=.2):
        if(tipo=="xpath"):
            try:
               # self.driver.switch_to.frame(0)
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element_by_xpath(selector)

                act=ActionChains(self.driver)
                act.move_to_element_with_offset(val,x,y).click().perform()
                print("clcik al elemento {} coordenada {}, {}".format(selector,x,y))
                t=time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("no se encuentra"+selector)
                return t
        if(tipo=="id"):
            try:

                #self.driver.switch_to.frame(0)   #con esto le digo que se vaya a esa ventana del iframe. el 0 es el primero que encuentre.
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element_by_id(selector)

                act= ActionChains(self.driver)
                act.move_to_element_with_offset(val, x, y).click().perform()    #cpn el click le dice que haga click y con el perform dice que lo ejecute a esa act
                print("click al elemento {}coordenada {},{}".format(selector,x,y))
                t=time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("no se encuentra"+selector)
                return t





















































