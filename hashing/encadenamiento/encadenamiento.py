import random
from nodo import Nodo

class TablaHashEnncadenamiento:
    __tabla: int
    __tamano: int
    __claves: int
    
    def __init__(self, cla):
        self.__claves = cla
        self.__tamano = self.__claves
        self.__tabla = [None for _ in range(self.__tamano)]
        
    def agregar(self, clave, indice):
        nodo = Nodo(clave)
        nodo.setSig(self.__tabla[indice])
        self.__tabla[indice] = nodo
       
        
    def divisionesSucesivas(self, clave):
        return int(clave % self.__tamano)
    
    def insertar(self, clave):
        indice = self.divisionesSucesivas(clave)
        self.agregar(clave, indice)
        print(f"Clave {clave} insertada en la posicion {indice}")
        
    def buscar(self, clave):
        indice = self.divisionesSucesivas(clave)
        actual = self.__tabla[indice]
        i=0
        try:
            while actual.getDato() != clave and actual.getSig() != None:
                actual = actual.getSig()
                i+=1
            print(f"Clave {clave} encontrada en la posicion {indice} en el nodo {i}")
        except IndexError:
            print(f"No se encontro la clave {clave}")
        
    def tabla(self):
       for i in range(self.__tamano):
            print(f"Índice {i}: ", end="")
            actual = self.__tabla[i]
            while actual is not None:
                print(f"{actual.getDato()} -> ", end="")
                actual = actual.getSig()
            print("None")
        
if __name__ == "__main__":
    tabla = TablaHashEnncadenamiento(20)
    
    def generarClave():
        return random.randint(0, 1000)
    
    for _ in range(50):
        tabla.insertar(generarClave())
        
    tabla.tabla()
    
    buscar = int(input("Clave a buscar: "))
    tabla.buscar(buscar)