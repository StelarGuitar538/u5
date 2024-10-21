import random
import numpy as np

class Bucket:
    __tabla: np.ndarray
    __claves: int
    __tamano: int
    __cantBuckets: int
    
    def __init__(self, cla, cb):
        self.__claves = cla
        self.__cantBuckets = cb
        self.__tamano = int(((self.__claves / self.__cantBuckets)) * 1.2)
        self.__tabla = np.zeros((self.__tamano, self.__cantBuckets))
        

    def divAreaPrimaria(self, clave):
        return int(clave % self.__tamano)
    
    def insertar(self, clave , c):
        indice = self.divAreaPrimaria(clave)
        tamano = int(self.__tamano * 0.8)
        i=0
        try:
                while self.__tabla[indice][i] != 0:
                    i+=1
                if self.__tabla[indice][i] == 0:
                    self.__tabla[indice][i] = clave
                    c+=1
                    print(f"Clave {clave} insertada en la posicion {indice} en el bucket {c}")
        except IndexError:
                indiceOverflow = tamano
                i=0
                try:
                    while self.__tabla[indiceOverflow][i] != 0:
                        indiceOverflow +=1
                        i+=1
                    self.__tabla[indiceOverflow][i] = clave
                    print(f"area primaria llena. clave {clave} insertada en el area de overflow en la posicion {indiceOverflow}")
                except IndexError:
                    print("tabla llena")
        return c

    def buscar(self, clave):
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
            print("clave no encontrada")
            

    
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
    
    for _ in range(100):
        c= b.insertar(b.generarClave(), c)
    
    b.mostrar()
    
    buscar = int(input("Clave a buscar: "))
    b.buscar(buscar)