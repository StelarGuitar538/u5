import random
import numpy as np

class Bucket:
    __tabla: np.ndarray
    __claves: int
    __tamano: int
    __cantBuckets: int
    __arregloAuxiliar: np.ndarray
    __indiceOverflow: int
    __areaPrimaria: int
    
    def __init__(self, cla, cb):
        self.__claves = cla
        self.__cantBuckets = cb
        self.__tamano = int(((self.__claves / self.__cantBuckets)) * 1.2)
        self.__tabla = np.zeros((self.__tamano, self.__cantBuckets))
        self.__arregloAuxiliar = np.zeros(self.__tamano)
        self.__indiceOverflow = self.__areaPrimaria
        self.__areaPrimaria = self.__tamano *0.8

    def divAreaPrimaria(self, clave):
        return int(clave % self.__areaPrimaria)
    
    def insertar(self, clave, c):
        indice = self.divAreaPrimaria(clave)
        if self.__arregloAuxiliar[indice] < self.__cantBuckets:
            j = self.__arregloAuxiliar[indice]
            self.__tabla[indice][j] = clave
            self.__arregloAuxiliar[indice] +=1
        else:
            j = self.__indiceOverflow
            while self.__arregloAuxiliar[j] >= self.__cantBuckets:
                j+=1
            if j < self.__tamano:
                self.__tabla[j][self.__arregloAuxiliar[j]] = clave


    '''def buscar(self, clave):
        indice = self.divAreaPrimaria(clave)
        tamano = int(self.__tamano * 0.8) 
        i=0
        try:
            while self.__tabla[indice][i] != clave:
                i+=1
            if indice < tamano:
                print(f"clave {clave} encontrada en el area primaria indice {indice}")
            elif indice > tamano:
                print(f"clave {clave} encontrada en el area overflow indice {indice - tamano}")
        except IndexError:
            print("clave no encontrada")'''
            
    def buscar(self, clave):
        indice = self.divAreaPrimaria(clave)
        tamano = int(self.__tamano * 0.8)
        indiceOverflow =tamano
        i=0
        while i < self.__cantBuckets:
            if self.__tabla[indice][i] == clave:
                return print(f"clave {clave} encontrada en el area primaria indice {indice}")
            i+=1

        while indiceOverflow < self.__tamano:
            i=0
            while i < self.__cantBuckets:
                if self.__tabla[indiceOverflow][i] == clave:
                    return print(f"clave {clave} encontrada en el area overflow indice {indiceOverflow}")
                i+=1
            indiceOverflow +=1

    def mostrar(self):
        tamano = int(self.__tamano * 0.8)
        print("area primaria")
        for bucket in self.__tabla[:tamano]:
            print(bucket)
        print(f"area overflow ")
        for bucket in self.__tabla[tamano:]:
            print(bucket)

        
    def generarClave(self):
        return random.randint(0, 1000)
    
 

if __name__ == "__main__":
    b = Bucket(100, 4)
    c=0
    
    for _ in range(90):
        c= b.insertar(b.generarClave(), c)
    
    b.mostrar()
    
    buscar = int(input("Clave a buscar: "))
    b.buscar(buscar)