import random
import numpy as np

class Da:
    __tamano: int
    __arreglo: np.ndarray
    __claves: int
    __fc: float
    
    def __init__(self, claves, fc):
        self.__claves = claves
        self.__fc = fc
        self.__tamano = int(self.__claves / self.__fc)
        self.__arreglo = np.zeros(self.__tamano)
        
    def div(self, claves):
        return int(claves % self.__tamano)
    
    def insertar(self, clave):
        indice = self.div(clave)
        pasos = 0
        if self.__arreglo[indice] == 0:
            self.__arreglo[indice] = clave
        else:
            while self.__arreglo[indice] != 0 and pasos < self.__tamano:
                indice = (indice +1) % self.__tamano
                pasos +=1
            if self.__arreglo[indice] == 0:
                self.__arreglo[indice] = clave
        
    def buscar(self, clave):
        indice = self.div(clave)
        pasos =0
        if self.__arreglo[indice] == clave:
            return indice
        else:
            while self.__arreglo[indice] !=clave and pasos < self.__tamano:
                indice = (indice +1) % self.__tamano
                pasos +=1
            if self.__arreglo[indice] == clave:
                return
            
    def primo(self, x):
        primo = None
        while primo ==None:
            i=2
            while i< x and x % i != 0:
                i += 1
            if i == x:
                primo = x
            else:
                x += 1
        return primo
            
if __name__ == "__main__":
    d = Da(50, 0.7)
    
    def gen():
        return random.randint(0, 100)
    
    for _ in range(50):
        d.insertar(gen())
        
    
        