import random
import numpy as np

class Bu:
    __tamano: int
    __claves: int
    __arreglo: np.ndarray
    __cb: int
    
    def __init__(self, claves, cb):
        self.__claves = claves
        self.__cb = cb
        self.__tamano = (self.__claves/self.__cb) * 1.2
        self.__arreglo = np.zeros(self.__tamano, self.__cb)
        
    def div(self,clave):
        return clave % self.__tamano
    
    def insertar(self, clave, c):
        indice = self.div(clave)
        tamano = self.__tamano * 0.8
        i=0
        
        try:
            while indice < tamano and self.__arreglo[indice][i] != 0:
                
        except IndexError:
            i=0
            over = tamano
            try:
                while over < self.__tamano and self.__arreglo[over, i] == 0:
                    self.__arreglo[over, i] = clave
                    c+=1
            except IndexError as e:
                print(e)
                
    def buscar(self, clave):
        indice = self.div(clave)
        tamano = self.__tamano * 0.8
        i=0
        try:
            while indice < tamano and self.__arreglo[indice, i] != clave:
                
        
                
        