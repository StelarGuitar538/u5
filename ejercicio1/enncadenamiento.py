import random

class TablaHashEnncadenamiento:
    __tabla: int
    __tamano: int
    __claves: int
    
    def __init__(self, cla):
        self.__claves = cla
        self.__tamano = self.__claves
        self.__tabla = [[] for _ in range(self.__tamano)]
       
        
    def divisionesSucesivas(self, clave):
        return int(clave % self.__tamano)
    
    def insertar(self, clave):
        indice = self.divisionesSucesivas(clave)
        self.__tabla[indice].append(clave)
        print(f"Clave {clave} insertada en la posicion {indice}")
        
    def buscar(self, clave):
        indice = self.divisionesSucesivas(clave)
        i=0
        try:
            while self.__tabla[indice][i] != clave:
                i+=1
            print(f"clave {clave} encontrada en la posicion de la tabla {indice} y en la posicion de la lista {i}")
        except IndexError:
            print(f"clave {clave} no encontrada")
            
    def tabla(self):
        print(self.__tabla)
        
if __name__ == "__main__":
    tabla = TablaHashEnncadenamiento(20)
    
    def generarClave():
        return random.randint(0, 1000)
    
    for _ in range(50):
        tabla.insertar(generarClave())
        
    tabla.tabla()
    
    buscar = int(input("Clave a buscar: "))
    tabla.buscar(buscar)