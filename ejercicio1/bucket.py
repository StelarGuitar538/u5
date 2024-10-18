import random
import numpy as np

class Bucket:
    __tabla: list
    __claves: int
    __overflow: int
    __tamano: int
    __cantBuckets: int
    __areaOverflow: list
    
    def __init__(self, cla, cb, overflow):
        self.__claves = cla
        self.__cantBuckets = cb
        self.__tamano = int((self.__claves / self.__cantBuckets))
        self.__overflow = int((overflow/100) * (self.__tamano))
        self.__tabla = [[] for _ in range(self.__tamano)]
        self.__areaOverflow = [[] for _ in range(self.__overflow)]
        
    def divAreaPrimaria(self, clave):
        return int(clave % self.__tamano)
    
    def divAreaOverflow(self, clave):
        return int(clave % self.__overflow)
    
    def insertar(self, clave , c):
        indice = self.divAreaPrimaria(clave)
        if len(self.__tabla[indice]) < self.__cantBuckets:
            self.__tabla[indice].append(clave)
            c+=1
            print(f"Clave {clave} insertada en la posicion {indice} en el bucket {c}")
        else:
            over = self.divAreaOverflow(clave)
            if len(self.__areaOverflow[over]) < self.__cantBuckets:
                self.__areaOverflow[over].append(clave)
                c+=1
                print(f"Clave {clave} insertada en la posicion {over} en el overflow {c}")
        return c
        
    def buscar(self, clave):
        indice = self.divAreaPrimaria(clave)
        i=0
        try:
            while self.__tabla[indice][i] != clave:
                i+=1
            print(f"Clave {clave} encontrada en la posicion {indice} en el bucket {i}")
        except IndexError:
            print(f"No se encontro la clave {clave} en el area primaria")
            try:
                over = self.divAreaOverflow(clave)
                i=0
                while self.__areaOverflow[over][i] != clave:
                    i+=1
                print(f"Clave {clave} encontrada en la posicion {over} en el bucket {i}")
            except IndexError:
                print(f"No se encontro la clave {clave} en el area overflow")
    
    
    def mostrar(self):
        print(f"area primaria \n {self.__tabla}")
        print(f"area overflow \n {self.__areaOverflow}")
        
    def generarClave(self):
        return random.randint(0, 1000)
    
 

if __name__ == "__main__":
    b = Bucket(100, 4, 20)
    c=0
    
    for _ in range(120):
        c= b.insertar(b.generarClave(), c)
    
    b.mostrar()
    
    buscar = int(input("Clave a buscar: "))
    b.buscar(buscar)