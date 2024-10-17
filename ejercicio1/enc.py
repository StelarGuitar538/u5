import random

class TablaHashEncadenamiento:
    def __init__(self, tamano):
        self.tamano = tamano
        self.tabla = [[] for _ in range(tamano)]  # Cada posición de la tabla es una lista

    # Método de plegado
    def funcion_hash(self, clave):
        clave_str = str(clave)
        partes = [int(clave_str[i:i+2]) for i in range(0, len(clave_str), 2)]  # Dividimos la clave en partes de 2 dígitos
        suma_partes = sum(partes)
        return suma_partes % self.tamano  # Retornamos el índice modulado por el tamaño de la tabla

    # Insertar una clave en la tabla
    def insertar(self, clave):
        indice = self.funcion_hash(clave)
        self.tabla[indice].append(clave)

    # Buscar una clave en la tabla
    def buscar(self, clave):
        indice = self.funcion_hash(clave)  # Obtenemos el índice de la clave
        pasos = 0
        for k in self.tabla[indice]:  # Recorremos la lista de sinónimos
            pasos += 1  # Contamos cada comparación
            if k == clave:
                return pasos  # Clave encontrada, devolvemos el número de comparaciones
        return pasos  # Clave no encontrada, devolvemos el número de comparaciones

    # Calcular la longitud de cada lista de claves sinónimas
    def longitud_listas(self):
        longitudes = [len(lista) for lista in self.tabla]
        return longitudes

    # Calcular el promedio de las longitudes de las listas
    def promedio_longitudes(self):
        longitudes = self.longitud_listas()
        total_listas = len([lista for lista in self.tabla if len(lista) > 0])  # Solo consideramos listas no vacías
        return sum(longitudes) / total_listas if total_listas > 0 else 0

    # Contar cuántas listas varían en hasta 3 unidades respecto al promedio
    def contar_listas_varianza(self):
        longitudes = self.longitud_listas()
        promedio = self.promedio_longitudes()
        contador = 0
        for longitud in longitudes:
            if abs(longitud - promedio) <= 3:  # Si la longitud difiere en hasta 3 unidades
                contador += 1
        return contador

# Función para generar claves aleatorias
def generar_claves_aleatorias(cantidad, rango=10000):
    return [random.randint(0, rango) for _ in range(cantidad)]

# Parámetros
tamano_tabla = 1000
cantidad_claves = 1000

# Crear la tabla hash
tabla_hash = TablaHashEncadenamiento(tamano_tabla)

# Generar claves aleatorias
claves = generar_claves_aleatorias(cantidad_claves)

# Insertar las claves en la tabla
for clave in claves:
    tabla_hash.insertar(clave)

# Buscar una clave
clave_a_buscar = random.choice(claves)  # Escogemos una clave al azar de las ya insertadas
resultado_busqueda = tabla_hash.buscar(clave_a_buscar)
print(resultado_busqueda)

# Buscar una clave que no esté en la tabla
clave_no_insertada = 66
resultado_busqueda = tabla_hash.buscar(clave_no_insertada)
print(resultado_busqueda)
