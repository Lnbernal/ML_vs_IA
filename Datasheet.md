Introducion
NumPy (Numerical Python) es una biblioteca de código abierto para Python que proporciona soporte para trabajar con vectores y matrices multidimensionales de alto rendimiento, junto con una colección de funciones matemáticas y lógicas para operarlas
A) Arreglos en Numpy

-Creación de arreglos

np.array(lista) → Crea un arreglo a partir de una lista o tupla.
ej:
import numpy as np  # Importamos la librería
# ============================
# 1. Creación de Arreglos
# ============================
print("=== Creación de Arreglos ===")
arreglo1 = np.array([1, 2, 3, 4, 5])
print("Arreglo desde lista:", arreglo1)

Esto nos devuelve:

=== Creación de Arreglos ===
Arreglo desde lista: [1 2 3 4 5]
-------------------------------------------------------------------------
-Matrices
np.zeros((m,n)) → Genera una matriz de ceros.
np.ones((m,n)) → Genera una matriz de unos.

ej
# ============================
# 2. Arreglos de ceros y unos
# ============================
print("\n=== Crear un arreglo de ceros y unos ===")
ceros = np.zeros((3,3))   # Matriz 3x3 de ceros
unos = np.ones((2,4))     # Matriz 2x4 de unos
print("Matriz de ceros:\n", ceros)
print("Matriz de unos:\n", unos)

esto nos devuelve
=== Crear un arreglo de ceros y unos ===
Matriz de ceros:
 [[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
Matriz de unos:
 [[1. 1. 1. 1.]
 [1. 1. 1. 1.]]
 ----------------------------------------------------------------------------------------------
 - Operaciones con arreglos

Podemos realizar operaciones aritméticas directamente entre arreglos, aplicándose elemento a elemento.

ej
# ============================
# 3. Operaciones con arreglos
# ============================
print("\n=== Operaciones con arreglos ===")
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
print("Arreglo a:", a)
print("Arreglo b:", b)

suma = a + b
multiplicacion = a * b
print("Suma:", suma)
print("Multiplicación:", multiplicacion)


Esto nos devuelve:

=== Operaciones con arreglos ===
Arreglo a: [10 20 30]
Arreglo b: [1 2 3]
Suma: [11 22 33]
Multiplicación: [10 40 90]
----------------------------------------------------------------------------------------------
- Estadísticos básicos

NumPy permite obtener medidas estadísticas de manera sencilla.

ej
# ============================
# 4. Estadísticos básicos
# ============================
print("\n=== Estadísticos básicos ===")
datos = np.array([5, 10, 15, 20, 25])
print("Datos:", datos)

promedio = np.mean(datos)
maximo = np.max(datos)
minimo = np.min(datos)
print("Promedio:", promedio)
print("Máximo:", maximo)
print("Mínimo:", minimo)


Esto nos devuelve:

=== Estadísticos básicos ===
Datos: [ 5 10 15 20 25]
Promedio: 15.0
Máximo: 25
Mínimo: 5