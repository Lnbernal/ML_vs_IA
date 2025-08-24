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