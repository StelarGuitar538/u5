import random
import numpy as np

class Bucket:
    __tabla: np.ndarray
    __claves: int
    __overflow: int
    __tamano: int
    __cantBuckets: int
    
    def __init__(self, cla, cb, overflow):
        self.__claves = cla
        self.__cantBuckets = cb
        self.__overflow = overflow/100 + 1
        self.__tamano = (self.__claves / self.__cantBuckets) * self.__overflow
        self.__tabla = np.zeros((self.__tamano, self.__cantBuckets), dtype=int)
        
    def divisionesSucesivas(self, clave):
        return int(clave % self.__tamano)
    
    def insertar(self, clave):
        indice = self.divisionesSucesivas(clave)
        c = 0
        if self.__tabla[indice, c] == 0:
            self.__tabla[indice, c] = clave
            print(f"Clave {clave} insertada en la posicion {indice} en el bucket {c}")
        else: