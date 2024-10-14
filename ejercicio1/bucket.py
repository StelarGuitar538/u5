import random

class TablaHashBuckets:
    def __init__(self, tamano_tabla, tamano_bucket):
        self.tamano_tabla = tamano_tabla
        self.tamano_bucket = tamano_bucket
        self.tabla = [[] for _ in range(tamano_tabla)]  # Creamos una lista de buckets (listas vacías)

    # Mejoramos la función de extracción para una mejor dispersión
    def funcion_hash(self, clave):
        clave_str = str(clave)
        # Tomamos varios fragmentos de la clave y los sumamos
        partes = [int(clave_str[i:i+2]) for i in range(0, len(clave_str), 2)]
        suma_partes = sum(partes)
        return suma_partes % self.tamano_tabla

    # Insertar una clave en la tabla hash con buckets
    def insertar(self, clave):
        indice = self.funcion_hash(clave)
        bucket = self.tabla[indice]
        
        if len(bucket) < self.tamano_bucket:
            bucket.append(clave)  # Insertar si el bucket no está lleno
            print(f"Clave {clave} insertada en el bucket {indice}")
        else:
            print(f"Bucket en índice {indice} está desbordado, no se puede insertar clave {clave}")

    # Buscar una clave en la tabla hash con buckets
    def buscar(self, clave):
        indice = self.funcion_hash(clave)
        bucket = self.tabla[indice]
        pasos = 0
        for k in bucket:  # Recorremos el bucket
            pasos += 1  # Contamos cada comparación
            if k == clave:
                return pasos  # Clave encontrada, devolvemos el número de comparaciones
        return pasos  # Clave no encontrada, devolvemos el número de comparaciones

    # Informar sobre los buckets desbordados
    def contar_buckets_desbordados(self):
        desbordados = 0
        for bucket in self.tabla:
            if len(bucket) == self.tamano_bucket:
                desbordados += 1
        return desbordados

    # Informar sobre los buckets subocupados (menos de la tercera parte ocupada)
    def contar_buckets_subocupados(self):
        subocupados = 0
        for bucket in self.tabla:
            if len(bucket) < (self.tamano_bucket // 3):
                subocupados += 1
        return subocupados

# Función para generar claves aleatorias
def generar_claves_aleatorias(cantidad, rango=100000):
    return [random.randint(0, rango) for _ in range(cantidad)]

# Parámetros
tamano_tabla = 100  # Tamaño de la tabla hash
tamano_bucket = 15   # Tamaño máximo de cada bucket
cantidad_claves = 1000

# Crear la tabla hash
tabla_hash = TablaHashBuckets(tamano_tabla, tamano_bucket)

# Generar claves aleatorias
claves = generar_claves_aleatorias(cantidad_claves)

# Insertar las claves en la tabla hash
for clave in claves:
    tabla_hash.insertar(clave)

# Buscar una clave aleatoria
clave_a_buscar = random.choice(claves)
resultado_busqueda = tabla_hash.buscar(clave_a_buscar)
print(resultado_busqueda)

# Informar sobre los buckets desbordados
buckets_desbordados = tabla_hash.contar_buckets_desbordados()
print(f"Cantidad de buckets desbordados: {buckets_desbordados}")

# Informar sobre los buckets subocupados
buckets_subocupados = tabla_hash.contar_buckets_subocupados()
print(f"Cantidad de buckets subocupados: {buckets_subocupados}")

b = tabla_hash.buscar(66)
print(f"Resultado de búsqueda: {b}")