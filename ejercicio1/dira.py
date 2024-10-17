import random

class TablaHash:
    def __init__(self, tamano):
        self.tamano = tamano
        self.tabla = [None] * tamano
        self.longitudes_busqueda = []

    def funcion_hash(self, clave):
        return clave % self.tamano

    def insertar(self, clave):
        indice = self.funcion_hash(clave)
        pasos = 0
        intentos = 0
        while self.tabla[indice] is not None:  # Mientras haya colisión
            pasos += 1
            intentos += 1
            if intentos >= self.tamano:  # Si hemos dado la vuelta completa, la tabla está llena
                raise Exception("Tabla hash llena. No se puede insertar más elementos.")
            indice = (indice + 1) % self.tamano  # Prueba lineal (suma 1)
        
        self.tabla[indice] = clave
        return pasos

    def buscar(self, clave):
        indice = self.funcion_hash(clave)
        pasos = 0
        intentos = 0
        while self.tabla[indice] is not None:
            pasos += 1  # Cada comparación cuenta
            if self.tabla[indice] == clave:
                return pasos  # Clave encontrada, devolvemos el número de comparaciones
            intentos += 1
            if intentos >= self.tamano:  # Evitar ciclos infinitos si la clave no está
                break
            indice = (indice + 1) % self.tamano  # Prueba lineal
        return pasos  # Clave no encontrada, devolvemos las comparaciones hechas


    def insertar_muchas_claves(self, claves):
        total_pasos = 0
        for clave in claves:
            pasos = self.insertar(clave)
            total_pasos += pasos
        return total_pasos / len(claves)  # Promedio de pasos por inserción

    def buscar_muchas_claves(self, claves):
        total_pasos = 0
        for clave in claves:
            pasos = self.buscar(clave)
            self.longitudes_busqueda.append(pasos)
            total_pasos += pasos
        return total_pasos / len(claves)  # Promedio de pasos por búsqueda

# Función para generar 1000 claves numéricas aleatorias
def generar_claves_aleatorias(cantidad, rango=10000):
    return random.sample(range(rango), cantidad)

# Comparar casos con tamaño de tabla no primo y primo
def comparar_tamano_tabla(tamano_no_primo, tamano_primo, claves):
    print("=== Comparación de Tablas Hash ===\n")
    
    # Caso 1: Tabla Hash con tamaño NO primo
    print(f"Tabla Hash con tamaño NO primo ({tamano_no_primo}):")
    tabla_no_primo = TablaHash(tamano_no_primo)
    promedio_pasos_insercion = tabla_no_primo.insertar_muchas_claves(claves)
    promedio_pasos_busqueda = tabla_no_primo.buscar_muchas_claves(claves)
    b = tabla_no_primo.buscar(66)
    print(f"  Promedio de pasos por inserción: {promedio_pasos_insercion}")
    print(f"  Promedio de pasos por búsqueda: {promedio_pasos_busqueda}")
    print(f"  Resultado de búsqueda: {b}")
    print("\n")

    # Caso 2: Tabla Hash con tamaño primo
    print(f"Tabla Hash con tamaño primo ({tamano_primo}):")
    tabla_primo = TablaHash(tamano_primo)
    promedio_pasos_insercion = tabla_primo.insertar_muchas_claves(claves)
    promedio_pasos_busqueda = tabla_primo.buscar_muchas_claves(claves)
    b = tabla_no_primo.buscar(66)
    print(f"  Promedio de pasos por inserción: {promedio_pasos_insercion}")
    print(f"  Promedio de pasos por búsqueda: {promedio_pasos_busqueda}")
    print(f"  Resultado de búsqueda: {b}")


# Generar 1000 claves numéricas aleatorias
claves = generar_claves_aleatorias(1000)

# Comparar los dos tamaños de tabla
comparar_tamano_tabla(tamano_no_primo=1000, tamano_primo=1009, claves=claves)
