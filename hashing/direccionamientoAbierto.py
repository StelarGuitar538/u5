
import random
import numpy as np

class Da:
    __tabla: np.ndarray
    __claves: int
    __tamano: int
    __factorDeCarga: float
    
    def __init__(self, fa, claves):
        self.__claves = claves
        self.__factorDeCarga = fa
        self.__tamano = int(self.__claves / self.__factorDeCarga) 
        self.__tabla = np.zeros((self.__tamano))
        
    def dvisionesSucesivas(self, clave):
        return int(clave % self.__tamano)
        
        
    def insertar(self, clave):
        indice = self.dvisionesSucesivas(clave)
        pasos = 0
        if self.__tabla[indice] == 0:
            self.__tabla[indice] = clave
            pasos += 1
            print(f"Clave {clave} insertada en la posicion {indice} despues de {pasos} pasos")
        else:
            while self.__tabla[indice] != 0 and pasos < self.__tamano:
                indice = (indice + 1) % self.__tamano
                pasos += 1
            if self.__tabla[indice] == 0:
                self.__tabla[indice] = clave
                print(f"Clave {clave} insertada en la posicion {indice} despues de {pasos} pasos")
            else:
                raise Exception("Tabla llena")

    def buscar(self, clave):
        indice = self.dvisionesSucesivas(clave)
        pasos = 0
        while clave != self.__tabla[indice]:
            indice = (indice + 1) % self.__tamano
            pasos += 1
            if pasos == self.__tamano:
                raise Exception("posicion no encontrada")
        print(f"Clave {clave} encontrada en la posicion {indice} despues de {pasos} pasos")
        
    def mostrar(self):
        for i in range(self.__tamano):
            print(f"{self.__tabla[i]}")
    
if __name__ == "__main__":
        da = Da(0.7, 50)
        
        def generarClave():
            return random.randint(0, 1000)
        
        for _ in range(50):
            da.insertar(generarClave())
            
        da.mostrar()
        
        claveBuscar = int(input("Clave a buscar: "))
        da.buscar(claveBuscar)