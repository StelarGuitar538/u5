from nodo import Nodo
import random

class Enca:
    __tabla: int
    __tamano: int
    __claves: int
    
    def __init__(self, clave):
        self.__claves = clave
        self.__tamano = self.__claves
        self.__tabla = [None for _ in range(self.__tamano)]
        
    def div(self,clave):
        return clave % self.__tamano
    
    def agregar(self, clave, indice):
        nodo = Nodo(clave)
        nodo.setSig(self.__tabla[indice])
        self.__tabla[indice] = nodo
    
    def insertar(self, clave):
        indice = self.div(clave)
        self.agregar(clave, indice)
        
    def buscar(self, clave):
        indice=  self.div(clave)
        i=0
        actual = self.__tabla[indice]
        while actual.getDato() != clave and actual.getSig() != None:
            actual = actual.getSig()
            i+=1
        if actual.getDato() == clave:
            return
    
    def mostrar(self):
        for i in range(self.__tamano):
            actual = self.__tabla[i]
            while self.__tabla[i] != None:
                print(f"{actual.getDato()} --> ", end="")
                actual = actual.get
        